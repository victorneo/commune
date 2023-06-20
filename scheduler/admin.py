from django.contrib import admin
from .models import ScheduledMessage


class ScheduledMessageAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at']
    list_display = ['id', 'guild_channel', 'message', 'publish_time', 'published']
    ordering = ['-publish_time']


admin.site.register(ScheduledMessage, ScheduledMessageAdmin)
