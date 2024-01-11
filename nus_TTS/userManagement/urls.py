from django.urls import path
from django.contrib.auth import views as auth_views
from userManagement import views

urlpatterns = [
    # path('', views.homepage, name='index'),
    # path('qODEA/', views.qodea_homepage, name='qODEA'),
    # path('', views.user_login, name='login'),
    path('usermanagement/', views.user_management, name='usermanagement'),
    path('usermanagement/Invite_user', views.user_page, name='usermanagement/Invite_user'),
    # path('usermanagement/create_user', views.user_creation_form, name='usermanagement/create_user'),
    path('usermanagement/admin', views.admin, name='usermanagement/admin'),
    path('usermanagement/manager', views.manager, name='usermanagement/manager'),
    path('usermanagement/user', views.user, name='usermanagement/user'),
    path('usermanagement/parent', views.parent, name='usermanagement/parent'),
    path('usermanagement/client', views.client, name='usermanagement/client'),
    # path('usermanagement/parentdata', views.addclientcompany, name='usermanagement/parentdata'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    # path('home', views.home_page, name='home')W
]
