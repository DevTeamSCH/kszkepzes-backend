from django.db import models
from django.core import validators

from account.models import Profile
from homework.models import Solution
from common.validators import FileSizeValidator


class Document(models.Model):
    uploaded_by = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    uploaded_at = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=150)
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
    )
    solution = models.ForeignKey(Solution, related_name='files', on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.name
