"""views.py"""
from rest_framework.exceptions import AuthenticationFailed
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Vacancy, Skills, Level
from django.db import transaction
# from django.contrib.auth.views import LoginView, LogoutView


def LoginPage(self, request):
    """get"""
    return render(request, 'login.html', {'valid': True})


def LoginView(self, request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username, type(username), password, type(password))
    if username and password:
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('menu')
        else:
            return render(request, 'login.html', {'valid': False})
    # Если поля пустые, отображаем форму логина
    return render(request, 'login.html', {'valid': False})


def LogoutView(self, request):
    logout(request)
    return redirect('')


def CreateUserView(self, request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    repeat_password = request.POST.get('repeat_password')
    staff = request.POST.get('recruiter')
    if staff is None:
        staff = False
    if repeat_password == password:
        try:
            user = User.objects.create(username=username, is_staff=staff)
            user.set_password(password)
            user.save()
            user = authenticate(
                request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('menu')
        except Exception as e:
            print(e)
            return render(request, 'registration.html',
                          {'valid': False, 'text': 'Пользователь сущесвтует'})
        return redirect('menu')
    else:
        return render(request, 'registration.html',
                      {'valid': False, 'text': 'Пароли не совпадают'})


def RegistrationPage(self, request):
    """get method"""
    return render(request, 'registration.html')


def MenuView(self, request):
    if request.user.is_authenticated:
        queryset = Vacancy.objects.all()
        return render(request, 'menu.html', {'queryset': queryset})
    else:
        return redirect('')


def RecruiterPage(self, request):
    if request.user.is_authenticated and request.user.is_staff:
        queryset = Vacancy.objects.filter(user=request.user.id)
        return render(request, 'recruiter.html', {'queryset': queryset})
    else:
        return redirect('')


def UserPage():
    pass


def FindVacancyPage():
    pass


def UpdateVacancyPage(self, request):
    vacancy_id = self.kwargs['pk']
    if request.user.is_authenticated and request.user.is_staff:
        vacancy = Vacancy.objects.get(id=vacancy_id)
        level = vacancy.level
        skills = level.skills
        return render(request, '')


def UpdateVacancyPageUp(self, request):
    vacancy_id = request.POST.get('name')
    if request.user.is_authenticated and request.user.is_staff:
        vacancy = Vacancy.objects.get(id=vacancy_id)
        pass


def DeleteVacancy():
    pass


def CreateVacancyPage(self, request):
    if request.user.is_authenticated and request.user.is_staff:
        return render(request, 'create_vacancy.html', {'status': True})
    else:
        return redirect('')


def CreateVacancyPagePO(self, request):
    name = request.POST.get('name')
    skills = request.POST.get('skills')
    level = request.POST.get('level')
    if request.user.is_authenticated and request.user.is_staff:
        try:
            with transaction.atomic():
                Vacancy.objects.create(
                    name=name,
                    user=request.user)
                vacancy_id = Vacancy.objects.get(
                    name=name, user=request.user)

                Skills.objects.create(vacancy=vacancy_id,
                                      name=skills)
                skills_id = Skills.objects.get(
                    vacancy=vacancy_id, name=skills)

                Level.objects.create(skills=skills_id, level=level)

                # transaction.commit()
                return redirect('recruiter')
        except Exception as e:
            print(e)
            # transaction.rollback()
            return render(request, 'create_vacancy.html',
                          {'status': False, 'text': e})
    else:
        return redirect('')


def ReadVacancyPage():
    pass
