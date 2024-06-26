# Generated by Django 4.2.4 on 2023-11-28 14:07

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(default='', max_length=12, validators=[app.models.phone_validate], verbose_name='Телефон')),
                ('code', models.CharField(max_length=6, verbose_name='Код')),
                ('status', models.BooleanField(default=False, verbose_name='Статус')),
                ('friend_code', models.CharField(max_length=6, verbose_name='Код друга')),
                ('auth_code', models.CharField(max_length=4, verbose_name='Код авторизации')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'db_table': 'Users',
            },
        ),
    ]
