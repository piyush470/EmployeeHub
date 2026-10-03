from django.contrib import admin

# Register your models here.
from .models import Employee,Department
# admin.site.register(Employee) another way to ragister
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('id','name','email','age','salary','address')
    search_fields=('name','email')
    ordering=('id',)

# @admin.register(Company)
# class Company(admin.ModelAdmin):
#     list_display=('id','C_name','Email','location','branch')
#     search_fields=('C_name','Email')
#     ordering=('id',)

@admin.register(Department)
class Department(admin.ModelAdmin):
    list_display=('D_name',)