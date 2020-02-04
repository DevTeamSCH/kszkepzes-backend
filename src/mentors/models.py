from django.db import models
from account.models import Profile


class Mentor(models.Model):
    mentor = models.ForeignKey(
        Profile,
        related_name="mentor",
        on_delete=models.DO_NOTHING,
    )
    name = models.CharField(null=False, max_length=200)
    text = models.TextField()
    image = models.ImageField(
        upload_to='mentors/images/', null=True, blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.name
