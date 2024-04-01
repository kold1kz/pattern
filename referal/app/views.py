"""views.py"""
import time
import random
import re
from string import ascii_uppercase
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status, generics, permissions, viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response, SimpleTemplateResponse
from rest_framework.renderers import TemplateHTMLRenderer

from .serializers import PhoneNumberFormSerializer, UserSerializer, RegisterterSerializer

from .forms import PhoneNumberForm, CodeVerifForm, FriendCodeForm
from .models import User


def send_verification_code() -> str:
    """return 4x code in terminal and phone"""
    time.sleep(1)
    gen_number = ''.join(str(random.randint(0, 9)) for _ in range(4))
    print(gen_number)
    return gen_number


def validate_phone(phone_number: str) -> bool:
    """check str for nimber"""
    pattern = r'^\+7|8\d{10}$'

    if re.match(pattern, phone_number) is None:
        return False
    return True


def get_verification_code(phone_number: str) -> str:
    """get user code verif form model(bd)"""
    try:
        user = User.objects.get(phone=phone_number)
        print(user)
        return user.code
    except ObjectDoesNotExist:
        return None


def add_verification_code(phone_number: str, code: str) -> str:
    """get user code verif form model(bd)"""
    try:
        user = User.objects.get(phone=phone_number)
        user.code = code
        user.save()
    except ObjectDoesNotExist:
        return None


def phone_is_created(phone_number: str) -> bool:
    """check for created user"""
    try:
        user = User.objects.filter(phone=phone_number)
        if user:
            return True
    except ObjectDoesNotExist:
        return False


def add_phone(phone_number: str) -> bool:
    """add user phone in registration"""
    try:
        user = User.objects.filter(phone=phone_number)
        if user:
            return False
        else:
            user = User(phone=phone_number)
            user.friend_code = friend_code_generate()
            user.save()
        return True
    except ObjectDoesNotExist:
        return False


def friend_code_generate() -> str:
    """generate friend code"""
    return ''.join(random.choice(ascii_uppercase) for i in range(6))


def get_friend_code(phone_number: str) -> str:
    """get friend code"""
    try:
        user = User.objects.filter(phone=phone_number)
        return user.friend_code
    except ObjectDoesNotExist:
        return None


class LoginPage(generics.CreateAPIView):
    """login page"""
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        """method get"""
        form = PhoneNumberForm()
        return render(request, 'verif_code.html', {'form': form})

    def post(self, request):
        """method post"""
        form = PhoneNumberForm()

        phone_number = request.data['phone_number']
        if validate_phone(phone_number=phone_number):
            if phone_is_created(phone_number=phone_number):
                verification_code = send_verification_code()
                request.session['phone_number'] = phone_number
                add_verification_code(
                    phone_number=phone_number, code=verification_code)
                return redirect('enter_verification_code')
            else:
                error_message = "Error: No User with this number"
                return render(request, 'input_phone.html', {'form': form, 'error_message': error_message})

        else:
            error_message = "Error: Phone number not correct"
            return Response(template_name='user_page.html', data={'form': form, 'error_message': error_message})


class RegisterPage(generics.CreateAPIView):
    """registrPage"""
    # permission_classes=[permissions.AllowAny]
    serializer_class = RegisterterSerializer

    def get(self, request):
        """get method"""
        if 'foo' in request.GET:
            self.post(request)
        else:
            form = PhoneNumberForm()
            return render(request, 'registration.html', {'form': form})

    def post(self, request):
        """post method"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        message = RegisterterSerializer(
            user, context=self.get_serializer_context()).data
        form = PhoneNumberForm()
        print(message)
        return render(request, 'registration.html', {'form': form, 'good_message': message})
        # return Response({
        #     "user": RegisterterSerializer(user, context=self.get_serializer_context()).data,
        #     "message": "Пользователь успешно создан",
        # })


class AddUser(generics.CreateAPIView):
    """add phone"""
    serializer_class = RegisterterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        pass

    def get(self, request):
        form = PhoneNumberForm()
        return render(request, 'registration.html', {'form': form})


def login(request):
    """enter phone number"""
    if request.method == 'POST':
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            if validate_phone(phone_number=phone_number):
                if phone_is_created(phone_number=phone_number):
                    verification_code = send_verification_code()
                    request.session['phone_number'] = phone_number
                    add_verification_code(
                        phone_number=phone_number, code=verification_code)
                    return redirect('enter_verification_code')
                else:
                    error_message = "Error: No User with this number"
                    return render(request, 'input_phone.html', {'form': form, 'error_message': error_message})

            else:
                error_message = "Error: Phone number not correct"
                return Response(template_name='user_page.html', data={'form': form, 'error_message': error_message})
                # return render(request, 'input_phone.html', {'form': form, 'error_message': error_message})
    if request.method == 'GET':
        form = PhoneNumberForm()
        response_data = {'form': form}
        return SimpleTemplateResponse(request, 'verif_code.html', response_data)
        # form = PhoneNumberForm()
        # return Response({'form': form}, template_name='verif_code.html')
        # return render(request, 'input_phone.html', {'form': form})
    return Response(template_name='user_page.html', data={'form': form})
    # return render(request, 'input_phone.html', {'form': form})


# @api_view(['GET', 'POST'])
# def registration(request):
#     """registration"""
#     if request.method == 'POST':
#         form = PhoneNumberForm(request.POST)
#         if form.is_valid():
#             phone_number = form.cleaned_data['phone_number']
#             if validate_phone(phone_number=phone_number):
#                 if add_phone(phone_number=phone_number):
#                     verification_code = send_verification_code()
#                     request.session['phone_number'] = phone_number
#                     add_verification_code(phone_number=phone_number, code=verification_code)
#                     messages.success(request, f'Регистрация успешна для номера: {phone_number}')
#                     return redirect('user_page')
#                 else:
#                     error_message = "Error: User with this phone already created"
#                     return render(request, 'registration.html', {'form': form, 'error_message': error_message})
#
#             else:
#                 error_message = "Error: Phone number not correct"
#                 return render(request, 'registration.html', {'form': form, 'error_message': error_message})
#     elif request.method == 'GET':
#         return render(request, 'registration.html', {'form': form})
#     else:
#         form = PhoneNumberForm()
#     return render(request, 'registration.html', {'form': form})


@api_view(['GET', 'POST'])
def enter_verification_code(request):
    """verif_code"""
    if request.method == 'POST':
        form = CodeVerifForm(request.POST)
        if form.is_valid():
            verif_code = form.cleaned_data['verif_code']
            phone_number = request.session.get('phone_number')
            verification_code = get_verification_code(phone_number)
            if verification_code is not None:
                if verif_code == verification_code:
                    messages.success(
                        request, f'Авторизация успешна для номера: {phone_number}')
                    return redirect('user_page')
                else:
                    print("error code verif")
                    error_message = "Error code verification"
                return render(request, 'verif_code.html', {'form': form, 'error_message': error_message})
    else:
        form = CodeVerifForm()
    return render(request, 'verif_code.html', {'form': form})


class MenuGet(generics.GenericAPIView):
    """menu"""
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        """get"""
        return render(request, 'menu.html')


class UserpageGet(generics.GenericAPIView):
    """user page"""

    def get(self, request):
        """get method"""
        return render(request, 'user_page.html')
