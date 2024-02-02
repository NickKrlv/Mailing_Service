from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    email_token = models.CharField(max_length=50, **NULLABLE, verbose_name='email_token')
    clients = models.ManyToManyField('mailing.Client', verbose_name='Клиенты')
    mails = models.ManyToManyField('mailing.MailingService', related_name='users', verbose_name='Рассылки')
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


