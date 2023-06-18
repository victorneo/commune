from django.contrib import admin
from .models import Guild, GuildChannel, GuildEvent


class GuildAdmin(admin.ModelAdmin):
    pass

class GuildChannelAdmin(admin.ModelAdmin):
    pass

class GuildEventAdmin(admin.ModelAdmin):
    pass


admin.site.register(Guild, GuildAdmin)
admin.site.register(GuildChannel, GuildChannelAdmin)
admin.site.register(GuildEvent, GuildEventAdmin)
