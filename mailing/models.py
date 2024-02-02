from django.db import models
from django.contrib.auth import get_user_model

NULLABLE = {'blank': True, 'null': True}

User = get_user_model()


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя', unique=True)
    email = models.EmailField(max_length=100, verbose_name='Email', unique=True)
    comment = models.TextField(verbose_name='Комментарий')
    creator = models.ForeignKey(User, default=1, on_delete=models.CASCADE, related_name='clients_created')

    def __str__(self):
        return f'{self.name} ({self.email})'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class MailingService(models.Model):
    daily = 'Раз в день'
    weekly = 'Раз в неделю'
    monthly = 'Раз в месяц'

    choices = (
        (daily, 'Раз в день'),
        (weekly, 'Раз в неделю'),
        (monthly, 'Раз в месяц')
    )

    created = 'Создана'
    started = 'Рассылка запущена'
    finished = 'Рассылка завершена'

    status_choices = (
        (created, 'Создана'),
        (started, 'Рассылка запущена'),
        (finished, 'Рассылка завершена'),
    )

    start_time = models.DateTimeField(verbose_name='Начало рассылки')
    end_time = models.DateTimeField(verbose_name='Окончание рассылки', null=True)
    status = models.CharField(max_length=50, choices=status_choices, default=created, verbose_name='Статус')
    mailing_period = models.CharField(max_length=50, choices=choices, default=daily, verbose_name='Период рассылки')
    clients = models.ManyToManyField(Client, verbose_name='Клиенты')
    creator = models.ForeignKey(User, default=1, on_delete=models.CASCADE, related_name='mailings_created')

    def __str__(self):
        return f'{self.start_time} - {self.end_time}. Статус: {self.status}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Message(models.Model):
    text = models.TextField(verbose_name='Текст сообщения', **NULLABLE)
    title = models.CharField(max_length=100, verbose_name='Тема письма')
    mailing = models.ForeignKey(MailingService, on_delete=models.CASCADE, verbose_name='Рассылка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Logs(models.Model):
    last_try = models.DateTimeField(verbose_name='Последняя попытка', auto_now_add=True)
    status = models.CharField(max_length=50, verbose_name='Статус')
    server_response = models.TextField(verbose_name='Ответ сервера', **NULLABLE)

    mailing = models.ForeignKey(MailingService, on_delete=models.CASCADE, verbose_name='Рассылка')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент', **NULLABLE)

    def __str__(self):
        return f'{self.last_try} - {self.status}'

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
