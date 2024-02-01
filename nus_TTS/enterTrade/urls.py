from django.urls import path
from . import views

urlpatterns = [
    path('enter_trade/', views.trade, name='enter_trade')
]
