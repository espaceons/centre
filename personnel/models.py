from django.db import models
from django.urls import reverse


class Personnel(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    fonction = models.CharField(max_length=100)
    date_embauche = models.DateField()

    # Relation Many-to-Many via le modèle Visite
    # CLÉ IMPORTANTE : Référence à 'entreprise.Entreprise'
    entreprises_visitees = models.ManyToManyField(
        'entreprise.Entreprise',
        through='Visite',
        related_name='visiteurs'
    )

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    def get_absolute_url(self):
        # Assurez-vous que le namespace est correct
        return reverse('personnel:detail_personnel', kwargs={'pk': self.pk})

# Modèle Visite


class Visite(models.Model):
    personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE)

    # CLÉ IMPORTANTE : Référence à 'entreprise.Entreprise'
    entreprise = models.ForeignKey(
        'entreprise.Entreprise', on_delete=models.CASCADE)

    date_visite = models.DateField()
    objet = models.CharField(max_length=255)
    rapport = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('personnel', 'entreprise', 'date_visite')
        ordering = ['-date_visite']

    def __str__(self):
        return f"Visite de {self.personnel.nom} à {self.entreprise.nom}"

    def get_absolute_url(self):
        return reverse('personnel:detail_personnel', kwargs={'pk': self.personnel.pk})
