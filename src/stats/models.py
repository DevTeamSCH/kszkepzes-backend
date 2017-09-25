from django.db import models

# Create your models here.
class User(models.Model):
    felhasznalo_nev = models.CharField(max_length=50)
    kepzes_eve = models.IntegerField()
    email_cim = models.EmailField()
    profilkep = models.ImageField()

    def __str__(self):
        return self.felhasznalo_nev

class Kepzes_alkalom(models.Model):
    idopont = models.DateField()
    letszam = models.IntegerField()
    resztvevok = models.ManyToManyField(User)
