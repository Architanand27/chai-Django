from django.urls import path
from . import views

urlpatterns = [
    path('', views.arc_home, name='arcHome'),
    
]
