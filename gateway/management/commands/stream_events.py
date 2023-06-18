from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from gateway.models import Event
from utils.discord_utils.gateway import get_streaming_client


class Command(BaseCommand):
    def handle(self, **options):
        client = get_streaming_client()

        @client.event
        async def on_ready():
            print(f'We have logged in as {client.user}')

        @client.event
        async def on_voice_state_update(member, before, after):
            print(member.guild)
            if after.channel:
                print(f'Member {member.name} joined {after.channel.name} at {timezone.now()}')
            else:
                print(f'Member {member.name} left {before.channel.name} at {timezone.now()}')

        client.run(settings.DISCORD_BOT_TOKEN)
