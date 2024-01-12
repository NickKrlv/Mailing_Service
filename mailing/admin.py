from django.contrib import admin
from mailing.models import Client, Message, Distribution, DistributionLog


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'full_name', 'comment',)
    list_filter = ('full_name',)
    search_fields = ('email', 'full_name', 'comment',)


@admin.register(Distribution)
class DistributionSettingsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'start_time', 'end_time', 'frequency', 'status',)
    list_filter = ('start_time', 'end_time', 'frequency', 'status',)
    search_fields = ('start_time', 'end_time',)


@admin.register(Message)
class MessageListSettingsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'body', 'distribution',)
    list_filter = ('distribution',)
    search_fields = ('title', 'body',)


@admin.register(DistributionLog)
class LogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'distribution', 'attempt_time', 'status', 'response',)
    list_filter = ('distribution', 'status',)
    search_fields = ('distribution__start_time', 'attempt_time', 'status',)
