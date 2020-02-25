import os

from django.db import models
from django.core import validators
from django.dispatch import receiver
from account.models import Profile
from homework.models import Solution
from common.validators import FileSizeValidator


def document_file_name(instance, filename):
    return '/'.join([
        'public/document',
        instance.solution.task.title,
        instance.uploaded_by.full_name,
        filename
    ])


class Document(models.Model):
    uploaded_by = models.ForeignKey(
        Profile,
        on_delete=models.DO_NOTHING,
        related_name='documents',
    )
    uploaded_at = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=150, blank=True, default='')
    description = models.TextField(blank=True, default='')
    file = models.FileField(
        validators=[
            validators.FileExtensionValidator([
                'png',
                'jpeg',
                'jpg',
                'zip',
            ]),
            FileSizeValidator(size_limit=52428800),  # 52428800 - 50MiB
        ],
        blank=True,
        null=True,
        upload_to=document_file_name
    )
    solution = models.ForeignKey(
        Solution, related_name='files', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Deletes file from filesystem when File object is deleted.
@receiver(models.signals.post_delete, sender=Document)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)
