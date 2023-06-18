from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from utils.discord_utils.gateway import get_streaming_client
from discord_guilds.models import GuildChannel, GuildChannelLog


class Command(BaseCommand):
    def handle(self, **options):
        client = get_streaming_client()

        @client.event
        async def on_ready():
            print(f'We have logged in as {client.user}')

        @client.event
        async def on_voice_state_update(member, before, after):
            if after.channel:
                print(f'Member {member.name} joined {after.channel.name} at {timezone.now()}')
                channel = after.channel
            else:
                channel = before.channel
                print(f'Member {member.name} left {before.channel.name} at {timezone.now()}')

            guild_channel = await GuildChannel.objects.select_related('guild').aget(discord_id=channel.id)
            await GuildChannelLog.objects.acreate(guild=guild_channel.guild, channel=guild_channel, num_users=len(channel.members))

        client.run(settings.DISCORD_BOT_TOKEN)
