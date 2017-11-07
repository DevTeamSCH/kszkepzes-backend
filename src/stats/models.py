from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    year_of_join = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    TEAMS = (
    ( 'DT', 'DevTeam'),
    ('NET', 'NeTeam'),
    ('ST','SecurITeam'),
    ('SYS','SysAdmin'),
    ('N','None'),
    )
    pref_group = models.CharField(max_length=10, choices = TEAMS, default = 'None')
    # Homeworks=models.ForeignKey(Homework)

    def __str__(self):
        return self.user.username


class KszkEvent(models.Model):
    date = models.DateField()
    visitors = models.ManyToManyField(User, related_name = 'visitor')

    num_of_pers = models.IntegerField()
