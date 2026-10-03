from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    age=models.IntegerField()
    salary=models.FloatField()
    designation=models.CharField(max_length=50)
    experience=models.FloatField()
    city=models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='employees/')
    status=models.CharField(max_length=25)
    department = models.ForeignKey('Department', 
                                   on_delete=models.CASCADE, 
                                   related_name='Employess',
                                   default=None,
                                   null=True, blank=True)
    address=models.TextField(max_length=255, default='Not Provided')
    
    
    # Company=models.ForeignKey('Company',
    #                           on_delete=models.CASCADE,
    #                           related_name='Employess',
    #                           default=None,null=True,blank=True)
    
    
    def __str__(self):
        return self.name


# class Company(models.Model):
#     C_name=models.CharField(max_length=50)
#     Email=models.EmailField(unique=True)
#     location=models.TextField(max_length=200)
#     branch=models.CharField(max_length=100)

   
#     def __str__(self):
#         return self.C_name

class Department(models.Model):
    D_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=15, unique=True)
    def __str__(self):
        return self.D_name