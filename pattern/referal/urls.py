"""
URL configuration for referal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views as app
from gpttest.views import TaskListView, TaskCreateView, TaskDetailAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)
from simple_chat.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', app.login, name='login'),
    path('enter_verification_code/', app.enter_verification_code,
         name='enter_verification_code'),
    path('registration/', app.RegisterPage.as_view(), name='registration'),
    path('api/token/', TokenObtainPairView.as_view(), name='token'),
    path('api/refresh_token/', TokenRefreshView.as_view(), name='refresh_token'),
    path('', app.MenuGet.as_view(), name='menu'),
    path('api/user_page', app.UserpageGet.as_view(), name='user_page'),
    path('api/login/', app.LoginPage.as_view(), name='login'),
    # path('api/registration/', app.RegisterPage.as_view(), name='registration'),
    path('api/back/add_user/', app.AddUser.as_view(), name='add_user'),
    path('api/gpttest/tasks/', TaskListView.as_view(), name="task-list"),
    path('api/gpttest/tasks/create/',
         TaskCreateView.as_view(), name="task-create"),
    path('api/gpttest/tasks/detail/<int:pk>/',
         TaskDetailAPIView.as_view(), name="task-detail")
]

urlpatterns += staticfiles_urlpatterns()
