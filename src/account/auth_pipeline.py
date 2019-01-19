from django.core import exceptions
from common.email import registration

from . import models


def create_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'authsch':
        try:
            user.profile
        except exceptions.ObjectDoesNotExist:
            models.Profile.objects.create(user=user)
            if user.email is not None:
                registration(user.email)
