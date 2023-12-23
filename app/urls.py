from django.urls import path
from . import views

urlpatterns = [
    path('EmailSend/', views.sendMail, name='sendemail'),  
    
]
