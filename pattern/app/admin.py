"""admin.py"""
from django.contrib import admin
from .models import Candidats, Vacancy, Level, Skills


# class UserAdmin(admin.ModelAdmin):
#     """add models to admin"""
#     list_dispaly = ('phone', 'code', 'status', 'friend_code', 'status_code')


class LevelInline(admin.TabularInline):
    model = Level
    extra = 1


class LevelSkils(admin.ModelAdmin):
    inlines = [LevelInline]


# Register your models here.
# admin.site.register(User, UserAdmin)
admin.site.register(Candidats)
admin.site.register(Vacancy)
admin.site.register(Skills, LevelSkils)
admin.site.register(Level)
