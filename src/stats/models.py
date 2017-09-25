from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    year_of_join = models.IntegerField()  # mikor csatlakozott a kszkepzeshez
    user = models.OneToOneField(User)  # django beépített user osztálya

    def __str__(self):
        return self.user.username


class Kszk_training(models.Model):
    date = models.DateField()
    num_of_pers = models.IntegerField()
    visitors = models.ManyToManyField(User)
