from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@sky.pro',
            is_active=True,
            is_superuser=True,
            is_staff=True,
        )

        user.set_password('5r36d6ft')
        user.save()

        self.stdout.write(self.style.SUCCESS('Admin created'))
