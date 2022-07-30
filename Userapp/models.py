from django.contrib.auth.models import User
from django.db import models

class Account(models.Model):
    ism = models.CharField(max_length=70)
    familya = models.CharField(max_length=70)
    email = models.EmailField()
    mamlakat = models.CharField(max_length=30)
    shahar = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userlar")

    def __str__(self):
        return self.ism