
from django.contrib import admin
from django.urls import path
from app import views as app
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', app.LoginPage.as_view(), name=''),
    path('admin/', admin.site.urls, name='admin'),
    path('login/', app.LoginView.as_view(), name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token'),
    path('api/refresh_token/', TokenRefreshView.as_view(),
         name='refresh_token'),
    path('api/registration/', app.RegistrationPage.as_view(),
         name='registration'),

    # path('', app.MenuGet.as_view(), name='menu'),
    # path('api/user_page', app.UserpageGet.as_view(), name='user_page'),
    # path('api/login/', app.LoginPage.as_view(), name='login'),
    # path('api/back/add_user/', app.AddUser.as_view(), name='add_user'),
    # path('api/gpttest/tasks/', TaskListView.as_view(), name="task-list"),
    # path('api/gpttest/tasks/create/',
    #      TaskCreateView.as_view(), name="task-create"),
    # path('api/gpttest/tasks/detail/<int:pk>/',
    #      TaskDetailAPIView.as_view(), name="task-detail")
]

urlpatterns += staticfiles_urlpatterns()
