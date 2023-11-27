"""admin.py"""
from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    """add models to admin"""
    list_dispaly=('phone', 'code', 'status', 'friend_code', 'status_code')

# Register your models here.
admin.site.register(User, UserAdmin)
