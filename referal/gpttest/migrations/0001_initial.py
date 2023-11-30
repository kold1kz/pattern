# Generated by Django 4.2.4 on 2023-11-28 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок задачи')),
                ('description', models.TextField(verbose_name='Описание')),
                ('status', models.CharField(choices=[('in_progress', 'В процессе'), ('complite', 'Завершено')], default='complite', max_length=20, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
    ]
