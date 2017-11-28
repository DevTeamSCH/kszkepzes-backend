from django.db import models
from account.models import Profile
from django.utils import timezone
from django.core.exceptions import ValidationError


class KszkEvent(models.Model):
    date = models.DateTimeField(null=False)
    visitors = models.ManyToManyField(Profile, related_name='visitor')

    def clean(self):
        if self.date > timezone.now():
            raise ValidationError('Invalid date')
