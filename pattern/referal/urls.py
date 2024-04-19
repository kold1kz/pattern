
from django.contrib import admin
from django.urls import path
from app import views as app
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', app.LoginPage.as_view(), name=''),
    path('admin/', admin.site.urls, name='admin'),
    path('login/', app.LoginView.as_view(), name='login'),
    path('logout/', app.LogoutView.as_view(), name='logout'),
    path('create_user/', app.CreateUserView.as_view(), name='create_user'),
    path('menu/', app.MenuView.as_view(), name='menu'),
    path('registration/', app.RegistrationPage.as_view(),
         name='registration'),
    path('recruiter', app.RecruiterPage.as_view(),
         name='recruiter'),
    path('user_page', app.UserPage.as_view(),
         name='user_page'),
    path('find_vacancy_page', app.FindVacancyPage.as_view(),
         name='find_vacancy_page'),
    path('recruiter/<int:pk>/update_vacancy_page', app.UpdateVacancyPage.as_view(),
         name='update_vacancy_page'),
    path('recruiter/<int:pk>/delete_vacancy', app.DeleteVacancy.as_view(),
         name='delete_vacancy'),
    path('recruiter/create_vacancy_page', app.CreateVacancyPage.as_view(),
         name='create_vacancy_page'),
    path('read_vacancy_page/<int:pk>/', app.ReadVacancyPage.as_view(),
         name='read_vacancy_page'),
]

urlpatterns += staticfiles_urlpatterns()
