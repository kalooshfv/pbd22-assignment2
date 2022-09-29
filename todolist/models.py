from enum import auto
from django.db import models
from django import forms
from django.contrib.auth.models import User
import datetime

# Create your models here.
class ToDoTask(models.Model):
    task_user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_date = models.DateTimeField(default = datetime.datetime.now)
    task_title = models.CharField(max_length = 64)
    task_description = models.TextField()
    task_isfinished = models.BooleanField(default = False)

