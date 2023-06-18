from django.urls import include, path
from .views import discord_callback, ListGuildChannels, ListScheduledMessages, ListChannelScheduledMessages


urlpatterns = [
    path("api/guilds/<str:guild_id>/channels", ListGuildChannels.as_view(), name="list-guild-channels"),
    path("api/guilds/<str:guild_id>/scheduled-messages", ListScheduledMessages.as_view(), name="list-scheduled-messages"),
    path("api/channels/<int:channel_id>/scheduled-messages", ListChannelScheduledMessages.as_view(), name="list-channel-scheduled-messages"),
    path("discord/callback", discord_callback, name="discord-callback"),
]
