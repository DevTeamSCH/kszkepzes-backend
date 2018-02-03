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
    motivation = models.TextField(null=True)
    nick = models.CharField(max_length=15, blank=True, null=True)
    signed = models.BooleanField(default=False, null=False)
    groups = models.ManyToManyField(GroupChoice, related_name='profiles')
    # Homeworks=models.ForeignKey(Homework)

    def __str__(self):
        return self.user.username


class Deadline(SingletonModel):
    deadline = models.DateTimeField(null=True)
