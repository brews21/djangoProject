from django.conf.urls import url
from django.urls import path
from basic_app import views
from django.conf.urls import include

app_name = 'basic_app'

urlpatterns = [
    path('',views.SchoolListView.as_view(),name="list"),
    path('<int:pk>/',views.SchoolDetailView.as_view(), name="detail")
]
