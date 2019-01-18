from django.core import exceptions
from django.core.mail import send_mail

from . import models


def create_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'authsch':
        try:
            user.profile
        except exceptions.ObjectDoesNotExist:
            models.Profile.objects.create(user=user)
            if user.email is not None:
                send_mail('TESZT', 'Attiss meleg!4!!', 'noreply@devteam.sch.bme.hu', [user.email, ])
