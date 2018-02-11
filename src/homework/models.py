from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core import validators
#from account.models import Profile
# from . import myfields


# 5MB - 5242880
__MAX_UPLOAD_SIZE = 5242880


def validate_deadline(deadline):
    if deadline <= timezone.now():
        raise ValidationError(_('Date must be greater than now'), code='invalid')


class Task(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    deadline = models.DateTimeField(validators=[validate_deadline])
    text = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING) #Profile
    files = models.FileField(
        validators=[validators.FileExtensionValidator(
            'image/png',
            'image/jpeg',
            'application/zip',
        )],
        blank=True,
    )

    def __str__(self):
        return self.title


class Solution(models.Model):
    task = models.ForeignKey(Task, related_name='task_solution', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='student_solution',  on_delete=models.CASCADE) # Profile
    date = models.DateTimeField(auto_now_add=True, editable=False)
    ready = models.BooleanField(default=False)
    accepted = models.BooleanField(default=False)
    files = models.FileField(
        validators=[validators.FileExtensionValidator(
            'image/png',
            'image/jpeg',
            'application/zip',
        )],
        blank=True,
    )
