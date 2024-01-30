from django.contrib import admin
from .models import MailingService, Message, Logs, Client
from users.models import User


@admin.register(MailingService)
class MailingServiceAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'status', 'mailing_period', )
    list_filter = ('status', 'mailing_period', )
    search_fields = ('start_time', 'end_time', 'status', 'mailing_period', )


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'mailing', )
    list_filter = ('mailing',)
    search_fields = ('title', 'mailing', )


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('last_try', 'status', 'mailing', 'client', )
    list_filter = ('status', 'mailing', 'client', )
    search_fields = ('last_try', 'status', 'mailing', 'client', )


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', )
    list_filter = ('email',)
    search_fields = ('name', 'email', )


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', )
    search_fields = ('email', )
