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
    # dokumentum kezeles

    def __str__(self):
        return self.title


class Solution(models.Model):
    task = models.ForeignKey(Task, related_name='task_solution', on_delete=models.CASCADE)
    created_by = models.ForeignKey(Profile, related_name='student_solution', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    accepted = models.BooleanField()
    files = models.FileField(
        validators=[
            validators.FileExtensionValidator([
                'png',
                'jpeg',
                'jpg',
                'zip',
            ]),
            FileSizeValidator(size_limit=52428800),  # 52428800 - 50MiB
        ],
    )

    def __str__(self):
        return "[{}] {}".format(self.created_at, self.created_by.full_name)
