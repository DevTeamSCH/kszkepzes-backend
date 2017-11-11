from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField()
    deadline = models.DateTimeField()
    text = models.TextField()
    author = models.OneToOneField(User)
    files = models.FileField()


# Normálisabb angol nevet adni ér!!
class Solution(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    date = models.DateTimeField()
    ready = models.BooleanField()
    files = models.FileField()


class Student(models.Model):
    user = models.OneToOneField(User)
    homework = models.ForeignKey(Solution,  on_delete=models.CASCADE)
