from django.urls import path
from . import views

urlpatterns = [
    path('', views.arc_home, name='arcHome'),
    path('<int:chai_id>/', views.chai_details, name='chai_details'),
    path('chai_stores/', views.chai_store_view, name='chai_stores'),
    
]
