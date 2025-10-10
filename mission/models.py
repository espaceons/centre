# app mission

from django.db import models
from django.urls import reverse


class Visite(models.Model):
    # Lien vers l'employé
    personnel = models.ForeignKey(
        'personnel.Personnel', on_delete=models.CASCADE,
        verbose_name="Personnel en Mission"
    )

    # Lien vers l'entreprise cible
    entreprise = models.ForeignKey(
        'entreprise.Entreprise', on_delete=models.CASCADE,
        verbose_name="Entreprise Cible"
    )

    # Date et heure de départ (Date de début de la mission)
    date_depart = models.DateTimeField(
        verbose_name="Date et Heure de Départ", null=True, blank=True
    )

    # Date et heure de retour (Date de fin de la mission)
    date_retour = models.DateTimeField(
        verbose_name="Date et Heure de Retour", null=True, blank=True
    )

    objet = models.CharField(
        max_length=255, verbose_name="Objet de la Mission")

    # Le rapport est optionnel initialement
    rapport = models.TextField(
        blank=True, null=True, verbose_name="Rapport de Mission")

    # Ancien champ conservé (non obligatoire) pour la compatibilité
    date_visite = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Mission / Visite"
        verbose_name_plural = "Missions / Visites"
        # Contrainte pour éviter deux missions identiques au même moment
        unique_together = ('personnel', 'entreprise', 'date_depart')
        ordering = ['-date_depart']

    def __str__(self):
        return f"Mission de {self.personnel} à {self.entreprise} le {self.date_depart.date()}"

    def get_absolute_url(self):
        # Redirection vers la liste des missions ou la page du personnel
        return reverse('personnel:detail_personnel', kwargs={'pk': self.personnel.pk})
    # Propriété utile pour obtenir le jour de la semaine du départ
