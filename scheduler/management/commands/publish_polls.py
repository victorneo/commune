from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from scheduler.models import ScheduledPoll
from utils.discord_utils.guilds import send_message_to_channel, create_thread_from_message, create_reactions_for_message


NUMBER_REACTIONS = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣']


class Command(BaseCommand):
    def handle(self, **options):
        now = timezone.now()

        qm = ScheduledPoll.objects.filter(published=False, publish_time__lte=now).select_related('guild_channel')
        scheduled_polls = list(qm)

        num_polls = len(scheduled_polls)
        print(f'Total scheduled polls: {num_polls}')

        count = 0

        for sp in scheduled_polls:
            resp = send_message_to_channel(settings.DISCORD_BOT_TOKEN, sp.guild_channel.discord_id, sp.message)
            count += 1
            print(f'Published {count} out of {num_polls} polls')

            msg_id = resp.json()['id']
            create_thread_from_message(settings.DISCORD_BOT_TOKEN, sp.guild_channel.discord_id, msg_id)

            if sp.reaction_type == 'yes_no':
                create_reactions_for_message(settings.DISCORD_BOT_TOKEN, sp.guild_channel.discord_id, msg_id, ['✅', '❎'])
            else:
                reactions = NUMBER_REACTIONS[:sp.num_options]
                create_reactions_for_message(settings.DISCORD_BOT_TOKEN, sp.guild_channel.discord_id, msg_id, reactions)


        qm.update(published=True)
