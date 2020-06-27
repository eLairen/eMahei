

from django.urls import path
from . import views


urlpatterns = [
    
    path('form', views.reviews, name ='reviews'),
    
  
    ]
