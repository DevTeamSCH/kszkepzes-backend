from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    join_date = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    TEAMS = (
     ('DT', 'DevTeam'),
     ('NET', 'NeTeam'),
     ('ST', 'SecurITeam'),
     ('SYS', 'SysAdmin'),
     ('N', 'None'),
    )
    pref_group = models.CharField(max_length=10, choices=TEAMS, default='None')
    # Homeworks=models.ForeignKey(Homework)

    def __str__(self):
        return self.user.username

# Create your models here.
