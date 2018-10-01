from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUser(AbstractUser, UserManager):
    name = models.CharField(max_length=255,blank=True, null=True)

    def __str__(self):
        return self.email


class Post(models.Model):
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.CharField(max_length=120)
    active = models.BooleanField()
    published = models.DateTimeField()


