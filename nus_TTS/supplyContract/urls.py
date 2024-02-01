from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('supplycontract/createcontract', views.contract, name ='supplycontract/createcontract'),
]