from django.db import models
from django.urls import reverse


class Personnel(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    fonction = models.CharField(max_length=100)
    iu = models.CharField()

    # Relation Many-to-Many via le modèle Visite
    # CLÉ IMPORTANTE : Référence à 'entreprise.Entreprise'
    entreprises_visitees = models.ManyToManyField(
        'entreprise.Entreprise',
        through='mission.Visite',
        related_name='visiteurs'
    )

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    def get_absolute_url(self):
        # Assurez-vous que le namespace est correct
        return reverse('personnel:detail_personnel', kwargs={'pk': self.pk})

# Modèle Visite
