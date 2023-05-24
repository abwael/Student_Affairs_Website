from django.db import models

# Create your models here.

class Student(models.Model):
    id = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=64)
    dateOfBirth = models.DateTimeField()
    email = models.CharField(max_length=64)
    GPA = models.FloatField()
    level = models.IntegerField()
    Status = models.BooleanField()
    phone = models.CharField(max_length=12)