from django.conf.urls import url
from django.urls import path
from first_app import views

# Temaplate tagging
app_name = 'first_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('users/', views.users, name='users'),
    path('formpage/', views.form_name_view, name='form_page'),
    path('other/', views.other, name='other'),
    path('relative_url_templates/', views.relative_url_templates, name='relative_url_templates'),
]
