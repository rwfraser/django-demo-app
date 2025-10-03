from django.urls import path
from . import views

app_name = 'demo'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('api/status/', views.api_status, name='api_status'),
]