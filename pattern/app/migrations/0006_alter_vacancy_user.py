# Generated by Django 4.2.4 on 2024-04-17 11:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_rename_skill_name_candidats_skill_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель вакансии'),
        ),
    ]
