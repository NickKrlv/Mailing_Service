from django.core.management.base import BaseCommand
from mailing.models import Client, Distribution, Message


class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **options):
        # Создание 10 клиентов
        clients = []
        for i in range(1, 11):
            client = Client.objects.create(
                email=f'client{i}@example.com',
                full_name=f'Client {i}',
                comment=f'Comment for client {i}'
            )
            clients.append(client)
            self.stdout.write(self.style.SUCCESS(f'Successfully created client: {client}'))

        # Создание 20 рассылок
        distributions = []
        for i in range(1, 21):
            distribution = Distribution.objects.create(
                start_time=f'2024-01-01 12:00:00',
                frequency='daily',
                status='created'
            )
            distribution.clients.set(clients[:i])
            distributions.append(distribution)
            self.stdout.write(self.style.SUCCESS(f'Successfully created distribution: {distribution}'))

            # Создание 2 сообщений для каждой рассылки
            for j in range(1, 3):
                message = Message.objects.create(
                    distribution=distribution,
                    title=f'Message {j} for distribution {i}',
                    body=f'Body of message {j} for distribution {i}'
                )
                self.stdout.write(self.style.SUCCESS(f'Successfully created message: {message}'))
