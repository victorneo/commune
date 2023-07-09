from django.contrib import admin
from django import forms
from .models import ScheduledMessage, ScheduledPoll


class ScheduledMessageAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at']
    list_display = ['id', 'guild_channel', 'message', 'publish_time', 'published']
    ordering = ['-publish_time']


class ScheduledPollAdminForm(forms.ModelForm):
    class Meta:
        model = ScheduledPoll
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['reaction_type'] == 'number' and cleaned_data['num_options'] is None:
            raise forms.ValidationError({'num_options': 'Must have at least one option for number polls'})

        if cleaned_data['reaction_type'] == 'yes_no':
            cleaned_data['num_options'] = None


class ScheduledPollAdmin(admin.ModelAdmin):
    form = ScheduledPollAdminForm

    readonly_fields = ['created_at', 'updated_at']
    list_display = ['id', 'guild_channel', 'message', 'publish_time', 'published', 'reaction_type', 'num_options']
    ordering = ['-publish_time']


admin.site.register(ScheduledMessage, ScheduledMessageAdmin)
admin.site.register(ScheduledPoll, ScheduledPollAdmin)
