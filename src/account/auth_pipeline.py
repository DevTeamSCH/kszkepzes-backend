from django.core import exceptions
from common.email import registration_email

from . import models


def create_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'authsch':
        if user.email is not None:
            registration_email(user.email)
        try:
            user.profile
        except exceptions.ObjectDoesNotExist:
            models.Profile.objects.create(user=user)
