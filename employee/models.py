from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    # personal details
    employee_name=models.CharField(max_length=100)
    employee_id=models.CharField(max_length=100, unique=True)
    phone=models.CharField(max_length=15)
    address=models.TextField()

    # job Details
    job_role=models.CharField(max_length=150)
    department=models.CharField(max_length=150)
    joining_date=models.DateField()

    #Professional
    experience=models.DecimalField(max_digits=4, decimal_places=1)
    skills=models.TextField()

    #Documents
    resume=models.FileField(upload_to='documents/', null=True, blank=True)
