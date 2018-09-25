from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.

class Post(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=120)
    active = models.BooleanField()
    published = models.DateTimeField()

