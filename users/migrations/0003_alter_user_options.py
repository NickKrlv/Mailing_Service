# Generated by Django 5.0.1 on 2024-02-05 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_mails'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('set_product_active', 'Can set product active')], 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]