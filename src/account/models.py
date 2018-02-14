from django.db import models
from django.contrib.auth.models import User
from solo.models import SingletonModel


class GroupChoice(models.Model):
    TEAMS = (
        ('DT', 'DevTeam'),
        ('NET', 'NeTeam'),
        ('ST', 'SecurITeam'),
        ('SYS', 'SysAdmin'),
        ('HAT', 'Hallgatói Tudásbázis'),
        ('N', 'None'),
    )
    choice = models.CharField(max_length=10, choices=TEAMS, default='N', unique=True)

    def __str__(self):
        return self.choice


class Profile(models.Model):
    join_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    # TODO: Change the default to json render side
    motivation_about = models.TextField(blank=True, default='')
    motivation_profession = models.TextField(blank=True, default='')
    motivation_exercise = models.TextField(blank=True, default='')
    nick = models.CharField(max_length=15, blank=True, default='')
    signed = models.BooleanField(default=False, null=False)
    groups = models.ManyToManyField(GroupChoice, related_name='profiles')

    @property
    def full_name(self):
        return self.user.get_full_name()

    def __str__(self):
        return self.full_name


class Deadline(SingletonModel):
    deadline = models.DateTimeField(null=True)
