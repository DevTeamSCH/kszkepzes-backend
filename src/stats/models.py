from django.db import models
from account.models import Profile
from common.middleware import CurrentUserMiddleware


class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField(null=False)
    description = models.TextField(blank=True, default='')
    visitors = models.ManyToManyField(
        Profile,
        related_name='events_visitor',
        blank=True
    )
    absent = models.ManyToManyField(
        Profile,
        related_name='events_absent',
        blank=True
    )
    created_by = models.ForeignKey(
        Profile,
        related_name='created_event',
        on_delete=models.DO_NOTHING,
        default=CurrentUserMiddleware.get_current_user_profile
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name


class Note(models.Model):
    event = models.ForeignKey(
        Event, related_name='notes', on_delete=models.CASCADE, blank=True, null=True)
    profile = models.ForeignKey(
        Profile, related_name='notes', on_delete=models.CASCADE, blank=True, null=True)
    note = models.TextField()
    created_by = models.ForeignKey(
        Profile,
        related_name='created_notes',
        on_delete=models.DO_NOTHING,
        default=CurrentUserMiddleware.get_current_user_profile
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.note
