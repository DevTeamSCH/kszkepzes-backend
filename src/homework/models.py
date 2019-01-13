from django.db import models
from django.core import validators

from common.validators import FileSizeValidator
from account.models import Profile



class Task(models.Model):
    created_by = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    title = models.CharField(max_length=150)
    text = models.TextField()
    deadline = models.DateTimeField()

    def __str__(self):
        return self.title


class Solution(models.Model):
    task = models.ForeignKey(Task, related_name='solution', on_delete=models.CASCADE)
    created_by = models.ForeignKey(Profile, related_name='solution', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    note = models.TextField()
    accepted = models.BooleanField()
    corrected = models.BooleanField()

    def __str__(self):
        return "[{}] {}".format(self.created_at, self.created_by.full_name)
