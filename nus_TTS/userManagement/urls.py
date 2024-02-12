from django.urls import path
from userManagement import views

urlpatterns = [
    path('usermanagement/', views.user_management, name='usermanagement'),
    path('usermanagement/Invite_user', views.user_page, name='usermanagement/Invite_user'),
    path('usermanagement/admin', views.admin, name='usermanagement/admin'),
    path('usermanagement/manager', views.manager, name='usermanagement/manager'),
    path('usermanagement/user', views.user, name='usermanagement/user'),
    path('usermanagement/parent', views.parent, name='usermanagement/parent'),
    path('usermanagement/client', views.client, name='usermanagement/client'),
    path('usermanagement/inactive_users', views.inactive_users, name='usermanagement/inactive_users'),
    path('activate/<uidb64>/<token>', views.activate_user, name='activate'),
    path('client_data', views.client_data, name='client_data'),
    path('usermanagement/edituser/<id>', views.edituser, name ='usermanagement/edituser'),
    path('usermanagement/disableuser/<id>', views.disableuser, name ='usermanagement/disableuser'),
    path('usermanagement/moveuser/<id>', views.moveuser, name ='usermanagement/moveuser'),
    path('usermanagement/activeuser/<id>', views.activeuser, name ='usermanagement/activeuser'),
    path('usermanagement/moveparentuser/<id>', views.moveparentuser, name ='usermanagement/moveparentuser'),
    path('usermanagement/move-client/<id>', views.moveclientuser, name ='usermanagement/moveclient'),


    # path('home', views.home_page, name='home')W
]
