from django.db import models


# Create your models here.
class Task(models.Model):
    """Task model"""
    STATUS_CHOICES = (
        ('in_progress', 'В процессе'),
        ('complite', 'Завершено'),
    )

    title = models.CharField(max_length=100, verbose_name='Заголовок задачи')
    description = models.TextField(verbose_name='Описание')
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='complite',
        verbose_name='Status'
    )

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.title
