import random
from string import ascii_uppercase
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
