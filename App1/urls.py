from django.contrib import admin
from django.urls import path,include
from App1.views import  *

urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact')
]