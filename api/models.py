from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
