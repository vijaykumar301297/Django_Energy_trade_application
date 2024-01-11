from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('createcompany/', views.addcompany, name='createcompany/'),
    path('createcompany/parent', views.parent, name='createcompany/parent'),
    path('createcompany/client', views.client, name='createcompany/client'),
    path('createcompany/addParent', views.addparentcompany, name='createcompany/addParent'),
    path('createcompany/addClient', views.addclientcompany, name='createcompany/addClient'),
    # path('addcompany/addClient', views.addclientcompany, name='addcompany/addClient'),


]