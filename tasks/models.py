from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    task = models.TextField()
    isdone = models.BooleanField(default=False, blank=True)
