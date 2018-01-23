from django.db import models
from django.contrib.auth.models import User




class Profile(models.Model):
    join_date = models.DateField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    nick = models.CharField(max_length=15, blank=True, null=True)
    signed = models.BooleanField(default=False, null=False)
    # Homeworks=models.ForeignKey(Homework)

    def __str__(self):
        return self.user.username



class GroupChoice(models.Model):
    TEAMS = (
        ('DT', 'DevTeam'),
        ('NET', 'NeTeam'),
        ('ST', 'SecurITeam'),
        ('SYS', 'SysAdmin'),
        ('HAT', 'Hallgatói Tudásbázis'),
        ('N', 'None'),
    )
    pref_group = models.CharField(max_length=10, choices=TEAMS, default='None')
    profile =  models.ForeignKey(Profile, related_name="preferd_groups")

    class Meta:
        unique_together = ('pref_group', 'profile')