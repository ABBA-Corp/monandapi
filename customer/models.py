from django.db import models
from django.contrib.auth.models import User


class CheckAccaunt(models.Model):
    phone = models.CharField(max_length=50, null=True, blank=True)
    key = models.CharField(max_length=20, null=True, blank=True)
    


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True)
    addres = models.CharField(max_length=1000, null=True)
