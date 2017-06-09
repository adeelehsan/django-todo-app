from __future__ import unicode_literals
# from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.utils.timezone import datetime
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=200, null=True)
    creation_date = models.DateField(auto_now=True)
    completion_date = models.DateField(null=True, blank=True)

    class Meta:
        permissions = (('can_view', 'can view all task'),)

    def __str__(self):
        return self.title


class User(AbstractUser):
    joining_date = models.DateField(auto_now=True)
