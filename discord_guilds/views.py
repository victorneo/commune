from datetime import datetime
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import User
from utils.discord_utils.auth import get_access_token
from utils.discord_utils.user import get_user_info
from utils.discord_utils.guilds import get_guild_channels

from .models import Guild, GuildChannel, GuildAdministrator


class ListGuildChannels(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, guild_id):
        # Return all guild channels in this guild
        guild = get_object_or_404(Guild, discord_id=guild_id)
        channels = guild.guildchannel_set.all()

        serialized = [{'id': c.id, 'name': c.name, 'discord_id': c.discord_id,
                       'type': c.channel_type} for c in channels]
        return Response(serialized)


class ListScheduledMessages(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, guild_id):
        # Return all scheduled messages in this guild
        guild = get_object_or_404(Guild, discord_id=guild_id)
        scheduled_messages = guild.scheduledmessage_set.\
            select_related('channel').all()

        serialized = [{'channel': sm.channel.name,
                       'scheduled_time': sm.scheduled_time,
                       'published': sm.published,
                       'message': sm.message, }
                      for sm in scheduled_messages]
        return Response(serialized)


class ListChannelScheduledMessages(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, channel_id):
        channel = get_object_or_404(GuildChannel, id=channel_id)

        message = request.data.get('message')
        scheduled_time = request.data.get('scheduled_time')
        scheduled_time = datetime.strptime(
            scheduled_time, '%Y-%m-%dT%H:%M:%S.%f%z')

        sm = ScheduledMessage.objects.create(
            guild=channel.guild, channel=channel, message=message,
            scheduled_time=scheduled_time)

        return Response('success')


def discord_callback(request):
    '''
    Callback Params: discord/callback?code=&guild_id=&permissions=
    '''

    # Step 1: Get the code from the request
    code = request.GET.get("code")

    # Step 2: Exchange the code for tokens
    token = get_access_token(settings.DISCORD_CLIENT_ID,
                             settings.DISCORD_CLIENT_SECRET, settings.DISCORD_REDIRECT_URI, code)

    # Step 3: Fetch user info from Discord
    user_info = get_user_info(token.access_token)

    # Step 4: Save user info in DB
    username = user_info.email

    try:
        admin = GuildAdministrator.objects.get(discord_id=user_info.id)
    except GuildAdministrator.DoesNotExist:
        user, user_created = User.objects.select_related('discord_admin').get_or_create(
            username=username,
            defaults={
                'email': user_info.email,
            }
        )

        if user_created:
            admin = GuildAdministrator(user=user, discord_id=user_info.id)
        else:
            admin = user.discord_admin
    else:
        user = admin.user
        user_created = False

    admin.access_token = token.access_token
    admin.refresh_token = token.refresh_token
    admin.save()

    # Step 5: Create associated guild in DB
    guild, guild_created = Guild.objects.get_or_create(
        discord_id=token.guild_info['id'],
        defaults={
            'name': token.guild_info['name'],
        }
    )
    guild.users.add(user)

    # Step 6: Create channels in guild
    discord_channels = get_guild_channels(
        settings.DISCORD_BOT_TOKEN, guild.discord_id)
    channels = []

    channel_ids = [c.discord_id for c in discord_channels]
    existing_qs = GuildChannel.objects.filter(discord_id__in=channel_ids)
    existing_channels = {e.discord_id: e for e in existing_qs.all()}

    for c in discord_channels:
        # Skip channel groups
        if c.channel_type == 4:
            continue

        if c.discord_id not in existing_channels:
            channels.append(GuildChannel(
                guild=guild,
                discord_id=c.discord_id,
                name=c.name,
                channel_type=c.channel_type))
        else:
            existing = existing_channels[c.discord_id]
            if c.name != existing.name:
                existing.name = c.name
                existing.save()

    GuildChannel.objects.bulk_create(channels)

    msg = 'You are {}, and are you a new account: {}. Guild {} is new: {}'.format(
        username, user_created, guild.discord_id, guild_created)
    return render(request, 'index.html', {'message': msg})
