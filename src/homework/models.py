from django.db import models
from django.core import validators

from common.validators import FileSizeValidator
from account.models import Profile


class Task(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    deadline = models.DateTimeField()
    text = models.TextField()
    created_by = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    files = models.FileField(
        validators=[
            validators.FileExtensionValidator([
                'image/png',
                'image/jpeg',
                'application/zip',
            ]),
            FileSizeValidator(size_limit=52428800),  # 52428800 - 50MiB
        ],
        blank=True,
    )

    def __str__(self):
        return self.title


class Solution(models.Model):
    task = models.ForeignKey(Task, related_name='task_solution', on_delete=models.CASCADE)
    created_by = models.ForeignKey(Profile, related_name='student_solution', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    ready = models.BooleanField(default=False)
    accepted = models.BooleanField(default=False)
    files = models.FileField(
        validators=[
            validators.FileExtensionValidator([
                'image/png',
                'image/jpeg',
                'zip',
            ]),
            FileSizeValidator(size_limit=52428800),  # 52428800 - 50MiB
        ],
        blank=True,
    )
