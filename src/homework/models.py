from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core import validators
from . import  myfields



# 5MB - 5242880
MAX_UPLOAD_SIZE = 5242880


def validate_deadline(date):
    if date <= timezone.now():
        raise ValidationError(_('Date must be greater than now'), code='invalid')


# def validate_file_size(file):
#     if file._size > MAX_UPLOAD_SIZE:
#         raise ValidationError(_('Please keep filesize under' + MAX_UPLOAD_SIZE))

class Task(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    deadline = models.DateTimeField(validators=[validate_deadline])
    text = models.TextField()
    created_by = models.ForeignKey(User)
    files = models.FileField(validators=[validators.FileExtensionValidator('image/png', 'image/jpeg', 'application/zip')],
                             blank=True,
    )
    # files = myfields.RestrictedFileField(
    #     content_types=['image/png', 'image/jpeg', 'application/zip'],
    #     max_upload_size=MAX_UPLOAD_SIZE,
    #     blank=True,
    #     null=True,
    # )
#    solution_file = models.BooleanField()
#
#
   # def deadline_clean(self):
   #     if self.deadline <= timezone.now():
   #         raise ValidationError(_('Invalid date'), code='invalid')


class Solution(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE,)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    ready = models.BooleanField()
    files = models.FileField(validators=[
        validators.FileExtensionValidator('image/png', 'image/jpeg', 'application/zip')],
        blank=True,
    )
    created_by = models.ForeignKey(User)
    # files = myfields.RestrictedFileField(
    #     content_types=['image/png', 'image/jpeg', 'application/zip'],
    #     max_upload_size=MAX_UPLOAD_SIZE,
    #     blank=True,
    # )


class Student(models.Model):
    user = models.OneToOneField(User)
    homework = models.ForeignKey(Solution,  on_delete=models.CASCADE)
