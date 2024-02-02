# Generated by Django 5.0.1 on 2024-02-02 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='title')),
                ('slug', models.CharField(blank=True, max_length=300, null=True, verbose_name='slug')),
                ('content', models.TextField(verbose_name='content')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='preview')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='date_created')),
                ('view_count', models.IntegerField(default=0, verbose_name='view_count')),
            ],
            options={
                'verbose_name': 'blog',
                'verbose_name_plural': 'blogs',
            },
        ),
    ]
