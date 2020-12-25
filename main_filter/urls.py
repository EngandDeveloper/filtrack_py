from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getData/', views.getData, name='getData'),
]