from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('createcompany/', views.addcompany, name='createcompany/'),
    path('createcompany/parent', views.parent, name='createcompany/parent'),
    path('createcompany/client', views.client, name='createcompany/client'),
    path('createcompany/addParent', views.addparentcompany, name='createcompany/addParent'),
    path('createcompany/addClient', views.addclientcompany, name='createcompany/addClient'),
    path('createcompany/edit-parent/<id>', views.edit_parent, name='createcompany/edit-parent'),
    path('createcompany/edit-client/<id>', views.edit_client, name='createcompany/edit-client'),
    # path('createcompany/parent_pa>', views.parent_pag, name='createcompany/parent_pa'),
    # path('createcompany/client_ca', views.client_pag, name='createcompany/client_ca'),
    # path('addcompany/addClient', views.addclientcompany, name='addcompany/addClient'),


]