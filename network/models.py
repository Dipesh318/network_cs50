from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class post(models.Model):
    user = models.CharField(max_length=20)
    content = models.CharField(max_length=320)
    time = models.DateTimeField(auto_now=True, blank=True)


class like(models.Model):
    post_id = models.IntegerField()
    user = models.CharField(max_length=20)

class following(models.Model):
    user = models.CharField(max_length=20)
    following = models.CharField(max_length=20)
