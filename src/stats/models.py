from django.db import models
from account.models import Profile
from django.utils import timezone
from django.core.exceptions import ValidationError


class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField(null=False)
    visitors = models.ManyToManyField(Profile, related_name='visitor')
    created_by = models.ForeignKey(Profile, related_name='created_event', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name


class Note(models.Model):
    event = models.ForeignKey(Event, related_name='notes_event', on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, related_name='notes_user', on_delete=models.CASCADE)
    note = models.TextField()
    created_by = models.ForeignKey(Profile, related_name='created_notes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.note
