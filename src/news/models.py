from django.db import models
from account.models import Profile


class Article(models.Model):
    author = models.ForeignKey(Profile, related_name="author")
    title = models.CharField(null=False, max_length=200)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
