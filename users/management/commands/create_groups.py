from django.core.management import BaseCommand
from users.models import User
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    def handle(self, *args, **options):
        group_normal = Group.objects.create(name='normal')
        view_permissions = Permission.objects.filter(codename__startswith='view_')
        group_normal.permissions.set(view_permissions)
        group_normal.save()

        group_moderator = Group.objects.create(name='moderator')
        perm_names =['view_client', 'view_message', "change_mailing", "set_active", "set_client", "view_stream",]
        permissions = []
        for perm_name in perm_names:
            permission = Permission.objects.get(codename=perm_name)
            permissions.append(permission)
        group_moderator.permissions.set(permissions)
        group_moderator.save()