from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Tenant(models.Model):
    """Represents a client or school."""
    name = models.CharField(max_length=255, unique=True)
    domain = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    """Student data linked to a tenant."""
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='students')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField()
    enrolled_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
