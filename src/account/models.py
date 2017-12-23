from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime


class Profile(models.Model):
    join_date = models.DateField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    TEAMS = (
        ('DT', 'DevTeam'),
        ('NET', 'NeTeam'),
        ('ST', 'SecurITeam'),
        ('SYS', 'SysAdmin'),
        ('HAT', 'Hallgatói Tudásbázis'),
        ('N', 'None'),
    )
    pref_group = models.CharField(max_length=10, choices=TEAMS, default='None')
    nick = models.CharField(max_length=15, blank=True, null=True)
    signed = models.BooleanField(default=False, null=False)
    # Homeworks=models.ForeignKey(Homework)

    def __str__(self):
        return self.user.username

    def clean(self):
        if self.join_date > datetime.date.today() or self.join_date < datetime.date(2015, 1, 1):
            raise ValidationError('Invalid date')
