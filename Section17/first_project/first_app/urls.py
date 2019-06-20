from django.conf.urls import url
from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('users/', views.users, name='users'),
]
