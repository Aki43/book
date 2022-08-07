from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('ukraine/', views.ukraine, name='ukraine'),
    path('create/', views.create, name='create')
]
