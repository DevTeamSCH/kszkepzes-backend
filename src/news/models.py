from django.db import models
from account.models import Profile
from common.middleware import CurrentUserMiddleware


class Article(models.Model):
    author = models.ForeignKey(
        Profile,
        related_name="author",
        on_delete=models.DO_NOTHING,
        default=CurrentUserMiddleware.get_current_user_profile
    )
    title = models.CharField(null=False, max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    updated_by = models.ForeignKey(
        Profile,
        related_name="updater",
        on_delete=models.DO_NOTHING,
        default=CurrentUserMiddleware.get_current_user_profile
    )

    def __str__(self):
        return self.title
