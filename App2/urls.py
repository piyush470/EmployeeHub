from django.contrib import admin
from django.urls import path,include
from .views import  *

urlpatterns = [
    path('',home,name='empdata'),
    path('empdata/',display,name='empdata'),
    path('form/',addEmpData,name='form'),
    path('edit/<int:id>/',updateEmpData,name='edit'),
    path('delete/<int:id>/',deleteEmpData,name='delete'),
    path('employee/<int:id>/', employeeDetails, name='employee_details'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]