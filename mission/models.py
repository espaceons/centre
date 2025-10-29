from django.db import models
from django.urls import reverse


class Visite(models.Model):

    # Définition des choix d'état
    ETAT_CHOICES = [
        ('PLANNIFIEE', 'Planifiée'),
        ('EN_COURS', 'En Cours'),
        ('REALISE', 'Realiser'),
        ('ANNULEE', 'Annulée'),
        ('NON_REALISER', 'Non Realiser'),
    ]

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
        verbose_name="Date et Heure de Départ", null=True, blank=True)

    # Date et heure de retour (Date de fin de la mission)
    date_retour = models.DateTimeField(
        verbose_name="Date et Heure de Retour", null=True, blank=True)
    lieu = models.CharField(
        max_length=255, verbose_name="Lieu de depart", null=True, blank=True)
    type_mission = models.CharField(
        max_length=255, verbose_name="Type de Mission", null=True, blank=True)
    moyen_transport = models.CharField(
        max_length=255, verbose_name="Moyen de Transport", null=True, blank=True)

    objet = models.CharField(
        max_length=255, verbose_name="Objet de la Mission")

    # Le rapport est optionnel initialement
    rapport = models.TextField(
        blank=True, null=True, verbose_name="Rapport de Mission")

    date_visite = models.DateField(null=True, blank=True)
    etat = models.CharField(
        max_length=50,
        choices=ETAT_CHOICES,
        default='PLANNIFIEE',
        verbose_name="État de la Mission"
    )

    class Meta:
        verbose_name = "Mission / Visite"
        verbose_name_plural = "Missions / Visites"
        # Contrainte pour éviter deux missions identiques au même moment
        unique_together = ('personnel', 'entreprise', 'date_depart')
        ordering = ['-date_depart']

    def __str__(self):
        # Vérifiez si date_depart est non nul avant d'appeler .date()
        date_str = self.date_depart.date() if self.date_depart else "Date inconnue"
        return f"Mission de {self.personnel} à {self.entreprise} le {date_str}"

    def get_absolute_url(self):
        # Redirection vers la liste des missions ou la page du personnel
        return reverse('personnel:detail_personnel', kwargs={'pk': self.personnel.pk})
