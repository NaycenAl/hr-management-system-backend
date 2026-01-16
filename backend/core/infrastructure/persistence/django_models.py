from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('RH', 'RH'),
        ('MANAGER', 'Manager'),
        ('EMPLOYEE', 'Employee'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='EMPLOYEE')


    employee_profile = models.OneToOneField(
        'EmployeeModel',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='user_account'
    )

    def __str__(self):
        return f"{self.username} ({self.role})"

class EmployeeModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"