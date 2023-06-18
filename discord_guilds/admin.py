from django.contrib import admin
from .models import DiscordGuild, DiscordGuildChannel, DiscordGuildEvent


class DiscordGuildAdmin(admin.ModelAdmin):
    pass

class DiscordGuildChannelAdmin(admin.ModelAdmin):
    pass

class DiscordGuildEventAdmin(admin.ModelAdmin):
    pass


admin.site.register(DiscordGuild, DiscordGuildAdmin)
admin.site.register(DiscordGuildChannel, DiscordGuildChannelAdmin)
admin.site.register(DiscordGuildEvent, DiscordGuildEventAdmin)
