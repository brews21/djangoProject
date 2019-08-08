from django.conf.urls import url
from django.urls import path
from theapp import views

# Template tagging
app_name = 'theapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
]
