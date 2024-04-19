"""models"""
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class Vacancy(models.Model):
    id = models.BigAutoField(primary_key=True,
                             verbose_name="Вакансия")
    name = models.CharField(verbose_name="Название", max_length=50)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Создатель вакансии", null=True,
        related_name='vacancy')

    class Meta:
        managed = True
        db_table = 'vacancy'
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return f'{self.name}'


class Skills(models.Model):
    id = models.BigAutoField(primary_key=True, default=None)
    vacancy = models.ForeignKey(
        Vacancy, verbose_name=("Вакансия"), on_delete=models.CASCADE,
        related_name='skills')
    name = models.CharField(verbose_name="Навык", max_length=50)

    class Meta:
        managed = True
        db_table = 'skills'
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"

    def __str__(self):
        return f'{self.name}'


class Level(models.Model):
    id = models.BigAutoField(primary_key=True, default=None)
    skills = models.ForeignKey(
        Skills, on_delete=models.CASCADE, related_name='level')
    level = models.CharField(verbose_name="Уровень владения", max_length=50)

    class Meta:
        managed = True
        db_table = 'level'
        verbose_name = "Уровень владения"
        verbose_name_plural = "Уровень владения"

    def __str__(self):
        return f'{self.level}'


class Candidats(models.Model):
    first_name = models.CharField(verbose_name="Имя", max_length=50)
    second_name = models.CharField(verbose_name="Фамилия", max_length=50)
    adress = models.CharField(verbose_name="Адрес", max_length=50,
                              blank=True, null=True)
    vacancy = models.ForeignKey(
        Vacancy, verbose_name="Вакансии", on_delete=models.CASCADE,
        related_name='candidats')
    skill = models.CharField(
        verbose_name="Навык", max_length=50)
    level = models.CharField(
        verbose_name="Уровень владения", max_length=50)

    class Meta:
        managed = True
        db_table = 'candidats'
        verbose_name = "Кандидат"
        verbose_name_plural = "Кандидаты"

    def __str__(self):
        return f'{self.second_name} {self.first_name}'
