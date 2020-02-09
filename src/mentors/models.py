import os

from django.db import models
from account.models import Profile
from django.dispatch import receiver


class Mentor(models.Model):
    mentor = models.ForeignKey(
        Profile,
        related_name="mentor",
        on_delete=models.DO_NOTHING,
    )
    name = models.CharField(null=False, max_length=200)
    text = models.TextField()
    image = models.ImageField(
        upload_to='public/mentors/images/', null=True, blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.name

# Deletes file from filesystem when File object is deleted.
@receiver(models.signals.post_delete, sender=Mentor)
def auto_delete_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
