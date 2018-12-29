from django.db import models

from account.models import Profile


class Document(models.Model):
    uploaded_by = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    uploaded_at = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=150)
    description = models.TextField()
    file = models.FileField()

    def __str__(self):
        return self.name
