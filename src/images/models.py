import os

from django.db import models
from django.dispatch import receiver


class Image(models.Model):
    image = models.ImageField(
        upload_to='public/images/', null=True, blank=True
        )

    def __str__(self):
        return str(self.id)

# Deletes file from filesystem when File object is deleted.
@receiver(models.signals.post_delete, sender=Image)
def auto_delete_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
