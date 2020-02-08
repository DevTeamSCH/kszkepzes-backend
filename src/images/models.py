from django.db import models


class Image(models.Model):
    image = models.ImageField(
        upload_to='public/images/', null=True, blank=True
        )

    def __str__(self):
        return str(self.id)
