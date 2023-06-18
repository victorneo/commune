from django.db import models
from users.models import User
from .managers import DiscordGuildEventManager


class DiscordGuildAdministrator(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, related_name='discord_admin')
    discord_id = models.CharField(max_length=255, null=False)
    discord_username = models.CharField(max_length=255, null=False)

    access_token = models.CharField(max_length=100, null=False)
    refresh_token = models.CharField(max_length=100, null=False)


class DiscordGuild(models.Model):
    discord_id = models.CharField(max_length=200, null=False, unique=True)
    name = models.CharField(null=False, max_length=200)
    users = models.ManyToManyField(User, related_name='guilds')

    def __str__(self):
        return f'{self.name}'


class DiscordGuildChannel(models.Model):
    guild = models.ForeignKey(DiscordGuild, on_delete=models.CASCADE)
    discord_id = models.CharField(max_length=200, null=False)
    name = models.CharField(null=False, max_length=200)
    channel_type = models.IntegerField(null=False)

    def __str__(self):
        return f'{self.guild.name} - {self.name} [{self.discord_id}]'


# Event id, name, when to add to Discord
class DiscordGuildEvent(models.Model):
    STAGE_INSTANCE = 1
    VOICE = 2
    EXTERNAL = 3
    CHOICES = (
        (STAGE_INSTANCE, 'Stage Instance'),
        (VOICE, 'Voice'),
        (EXTERNAL, 'External'),
    )

    guild = models.ForeignKey(DiscordGuild, on_delete=models.CASCADE)
    channel_id = models.TextField(null=True)

    name = models.TextField(null=False)

    publish_time = models.DateTimeField(null=False)
    published = models.BooleanField(default=False)

    scheduled_start_time = models.DateTimeField(null=False)
    scheduled_end_time = models.DateTimeField(null=False)

    event_type = models.IntegerField(
        null=False, choices=CHOICES, default=STAGE_INSTANCE)
    privacy_level = models.IntegerField(null=False, default=2)

    description = models.TextField(null=False)

    objects = DiscordGuildEventManager()


    def __str__(self):
        return f'{self.name} on {self.scheduled_start_time}'
