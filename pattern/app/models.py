"""models"""
import re
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy


# def phone_validate(phone: str):
#     """func for validate correct RUS number"""
#     pattern = r'^\+7|8\d{10}$'

#     if re.match(pattern, phone) is None:
#         raise ValidationError(gettext_lazy('%(phone)s is wrong'),
#                               params={'phone': phone},
#                               )


# class UserManager(models.Manager):
#     """user manager"""
#     pass


# class User(models.Model):
#     """Пользователь"""

#     class Meta:
#         """special class for admin panel"""
#         db_table = "Users"
#         verbose_name = "Пользователь"
#         verbose_name_plural = "Пользователи"

#     phone = models.CharField(
#         verbose_name="Телефон", max_length=12, default='', validators=[phone_validate])
#     code = models.CharField(verbose_name="Код", max_length=6)
#     status = models.BooleanField(verbose_name="Статус", default=False)
#     friend_code = models.CharField(verbose_name="Код друга", max_length=6)
#     auth_code = models.CharField(verbose_name="Код авторизации", max_length=4)

#     objects = UserManager()

#     def __str__(self):
#         return f'{self.phone} {self.code} {self.status} {self.friend_code} {self.auth_code}'


class Vacancy(models.Model):
    vacancy = models.IntegerField(
        verbose_name="Вакансия")
    vacancy_name = models.CharField(verbose_name="Название", max_length=50)

    class Meta:
        managed = True
        db_table = 'vacancy'
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return f'{self.vacancy_name}'


class Skills(models.Model):
    skill = models.BigAutoField(primary_key=True, default=None)
    vacancy = models.ForeignKey(
        Vacancy, verbose_name=("Вакансия"), on_delete=models.CASCADE)
    skill_name = models.CharField(verbose_name="Навык", max_length=50)

    class Meta:
        managed = True
        db_table = 'skills'
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"

    def __str__(self):
        return f'{self.skill_name}'


class Level(models.Model):
    skill = models.ForeignKey(Skills, on_delete=models.CASCADE)
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
        Vacancy, verbose_name="Вакансия", on_delete=models.CASCADE)
    skill_name = models.CharField(
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
