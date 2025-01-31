import random
from string import ascii_uppercase
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
# from .models import User



# class UserSerializer(serializers.ModelSerializer):
#     """user serializer"""
#     class Meta:
#         """meta"""
#         model = User
#         fields = ('phone', 'friend_code', 'status')

# class PhoneNumberFormSerializer(serializers.ModelSerializer):
#     """phone number serializer"""
#     class Meta:
#         """meta"""
#         model = User
#         fields = ('phone', 'auth_code')
    


# class RegisterterSerializer(serializers.ModelSerializer):
#     """register serializer"""
#     phone = serializers.CharField(write_only=True)

#     class Meta:
#         """meta"""
#         model = User
#         fields = [
#             "phone", "friend_code"
#         ]
#         extra_kwargs = {"friend_code":{"read_only":True}}

#     def create(self, validated_data):
#         """def create"""
#         phone_number = validated_data['phone']
#         friend_code = ''.join(random.choice(ascii_uppercase) for i in range(6))
#         try:
#             user = User.objects.get(phone=phone_number)
#             if phone_number == user.phone:
#                 # return "error, User already created"
#                 raise serializers.ValidationError({"error": "User already created"})
#         except ObjectDoesNotExist:
#             user2 = User(phone=phone_number, friend_code=friend_code)
#             user2.save()
#             print(user2)
#             return user2

# class RegisterterSerializer2(serializers.ModelSerializer):
#     """registerser2"""
#     pass

# class RegisterSerializer(serializers.Serializer):
#     """testSerializer"""

