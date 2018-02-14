from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError


class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField(null=False)
    visitors = models.ManyToManyField(User, related_name='visitor')

    def clean(self):
        if self.date > timezone.now():
            raise ValidationError('Invalid date')

    def __str__(self):
        return self.name
