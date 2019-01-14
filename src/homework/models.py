from django.db import models
from common.middleware import CurrentUserMiddleware
from account.models import Profile


class Task(models.Model):
    created_by = models.ForeignKey(
        Profile,
        on_delete=models.DO_NOTHING,
        related_name='tasks',
        default=CurrentUserMiddleware.get_current_user_profile,
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    title = models.CharField(max_length=150)
    text = models.TextField()
    deadline = models.DateTimeField()

    def __str__(self):
        return self.title


class Solution(models.Model):
    task = models.ForeignKey(Task, related_name='solutions', on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        Profile,
        related_name='solution',
        on_delete=models.DO_NOTHING,
        default=CurrentUserMiddleware.get_current_user_profile,
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    note = models.TextField()
    accepted = models.BooleanField()
    corrected = models.BooleanField()

    def __str__(self):
        return "[{}] {}".format(self.created_at, self.created_by.full_name)
