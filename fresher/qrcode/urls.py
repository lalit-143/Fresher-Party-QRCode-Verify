from django.contrib import admin
from django.urls import path
from qrcode import views

urlpatterns = [
    path('', views.home, name="home"),
    path('checknum/<str:num>', views.check_num, name="check_number"),
]