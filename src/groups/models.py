from django.db import models

# KSZK groups, like Devteam, Sysadmin, ...


class Group(models.Model):
    name = models.CharField(max_length=50, blank=True, default='')
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name
