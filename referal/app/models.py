"""models"""
import re
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy


def phone_validate(phone: str):
    """func for validate correct RUS number"""
    pattern = r'^\+7|8\d{10}$'

    if re.match(pattern, phone) is None:
        raise ValidationError(gettext_lazy('%(phone)s is wrong'),
                              params={'phone': phone},
                              )


class UserManager(models.Manager):
    """user manager"""
    pass


class User(models.Model):
    """Пользователь"""

    class Meta:
        """special class for admin panel"""
        db_table = "Users"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    phone = models.CharField(
        verbose_name="Телефон", max_length=12, default='', validators=[phone_validate])
    code = models.CharField(verbose_name="Код", max_length=6)
    status = models.BooleanField(verbose_name="Статус", default=False)
    friend_code = models.CharField(verbose_name="Код друга", max_length=6)
    auth_code = models.CharField(verbose_name="Код авторизации", max_length=4)

    objects = UserManager()

    def __str__(self):
        return f'{self.phone} {self.code} {self.status} {self.friend_code} {self.auth_code}'
