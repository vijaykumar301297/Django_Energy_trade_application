from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('home', views.home_page, name='home/'),
    path('', views.user_login, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='loginpage/passwordreset.html'),name='reset_password'),
    path('password_reset_done/',
         auth_views.PasswordResetDoneView.as_view(template_name='loginpage/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='loginpage/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='loginpage/password_reset_complete.html'),
         name='password_reset_complete'),
]