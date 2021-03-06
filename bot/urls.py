from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hook/', views.hook, name='hook'),
    path('interactive/', views.interactive, name='interactive'),
    path('command/', views.command, name='command'),
]
