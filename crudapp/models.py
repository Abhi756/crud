
from django.db import models

class EmployeeDetails(models.Model):
    Emp_ser=models.CharField(max_length=10)
    NAME=models.CharField(max_length=10)
    DESGN=models.CharField(max_length=10)
    Qualification=models.CharField(max_length=10)
    



