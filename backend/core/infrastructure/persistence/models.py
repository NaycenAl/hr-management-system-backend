from django.contrib.auth.models import AbstractUser
from django.db import models


class EmployeeModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    hire_date = models.DateField()


class UserModel(AbstractUser):

    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('RH', 'RH'),
        ('MANAGER', 'Manager'),
        ('EMPLOYEE', 'Employee'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='EMPLOYEE')

    employee = models.OneToOneField(
        EmployeeModel,   # 👈 PAS string
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )