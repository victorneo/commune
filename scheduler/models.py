from django.db import models
from discord_guilds.models import GuildChannel


class ScheduledMessage(models.Model):
    guild_channel = models.ForeignKey(GuildChannel, null=True, blank=False, on_delete=models.CASCADE)
    message = models.TextField(null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    published = models.BooleanField(default=False)
    publish_time = models.DateTimeField()

    def __str__(self):
        return f'Scheduled message for {self.guild_channel} at {self.publish_time}'
