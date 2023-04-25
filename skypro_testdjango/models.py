from django.contrib.auth.models import User
from django.db import models


class Data(models.Model):
    status = models.CharField(max_length=30)
    grade = models.CharField(max_length=30)
    specialty = models.CharField(max_length=30)
    salary = models.IntegerField()
    education = models.CharField(max_length=30)
    experience = models.TextField()
    portfolio = models.TextField
    title = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    author = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)
