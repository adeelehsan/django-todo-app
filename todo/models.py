from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Task(models.Model):

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    due_date = models.DateTimeField()

    def __str__(self):
        return self.title
