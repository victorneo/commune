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


class ScheduledPoll(models.Model):
    POLL_TYPES = [('yes_no', 'Yes/No'), ('number', 'Numbers')]
    NUM_CHOICES = [(None, 0), (1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7)]

    guild_channel = models.ForeignKey(GuildChannel, null=True, blank=False, on_delete=models.CASCADE)
    message = models.TextField(null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    published = models.BooleanField(default=False)
    publish_time = models.DateTimeField()

    reaction_type = models.CharField(max_length=20, null=False, default='yes_no', choices=POLL_TYPES)
    num_options = models.IntegerField(default=None, choices=NUM_CHOICES, null=True, blank=True)

    def __str__(self):
        return f'Scheduled poll for {self.guild_channel} at {self.publish_time}'
