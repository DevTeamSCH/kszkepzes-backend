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
    join_date = models.DateField(auto_now=True)
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    motivation = models.TextField(null=True)
    nick = models.CharField(max_length=15, blank=True, null=True)
    signed = models.BooleanField(default=False, null=False)
    groups = models.ManyToManyField(GroupChoice, related_name='profiles')
    # Homeworks=models.ForeignKey(Homework)

    def __str__(self):
        return self.user.username


class Deadline(SingletonModel):
    deadline = models.DateField(null=True)
