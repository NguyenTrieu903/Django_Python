from django.db import models
from django.db.models.base import Model
# Create your models here.


class postion (models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Employee (models.Model):
    fullName = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(postion, on_delete=models.CASCADE)
