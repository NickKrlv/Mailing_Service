from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Client(models.Model):
    email = models.EmailField(max_length=50, verbose_name='Электронная почта', unique=True)
    full_name = models.CharField(max_length=100, verbose_name='Полное имя')
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.full_name} ({self.email})'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Distribution(models.Model):

    frequency_choices = [
        ('daily', 'Раз в день'),
        ('weekly', 'Раз в неделю'),
        ('monthly', 'Раз в месяц'),
    ]

    status_choices = [
        ('created', 'Создана'),
        ('started', 'Запущена'),
        ('completed', 'Завершена'),
    ]

    start_time = models.DateTimeField(verbose_name='Начало рассылки')
    end_time = models.DateTimeField(verbose_name='Окончание рассылки', **NULLABLE)
    frequency = models.CharField(max_length=10, choices=frequency_choices, verbose_name='Частота рассылки')
    status = models.CharField(max_length=10, choices=status_choices, default='created', verbose_name='Статус')

    clients = models.ManyToManyField(Client, verbose_name='Клиенты')

    def __str__(self):
        return f'time: {self.start_time} - {self.end_time}, frequency: {self.frequency}, status: {self.status}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Message(models.Model):
    distribution = models.ForeignKey(Distribution, on_delete=models.CASCADE, verbose_name='Рассылка',
                                     related_name='messages', **NULLABLE)
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class DistributionLog(models.Model):
    distribution = models.ForeignKey(Distribution, on_delete=models.CASCADE, verbose_name='Рассылка')
    attempt_time = models.DateTimeField(verbose_name='Время попытки', auto_now=True)
    status = models.CharField(max_length=255, verbose_name='Статус')
    response = models.TextField(verbose_name='Ответ', **NULLABLE)

    def __str__(self):
        return f'{self.attempt_time} - {self.status}'

    class Meta:
        verbose_name = 'Лог рассылки'
        verbose_name_plural = 'Логи рассылок'
