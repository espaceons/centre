from django.db import models

# Create your models here.


class Entreprise(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    secteur_activite = models.CharField(max_length=100)
    delegation = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nom
