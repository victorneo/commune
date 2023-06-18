from django.core.management.base import BaseCommand
from django.conf import settings
from gateway.models import Event
from discord_utils.gateway import get_streaming_client


class Command(BaseCommand):
    def handle(self, **options):
        client = get_streaming_client()

        @client.event
        async def on_ready():
            print(f'We have logged in as {client.user}')


        @client.event
        async def on_message(message):
            print(message.content)
            print(message.guild)

        client.run(settings.DISCORD_BOT_TOKEN)
