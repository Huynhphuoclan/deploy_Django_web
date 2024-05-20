from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('base/', views.base, name = 'base'),
    path('demo/', views.demo, name = 'demo'),
    path('demo/', views.image_upload_view, name='demo'),
]