from django.db import models
from django.urls import reverse

# Create your models here.


class Entreprise(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    secteur_activite = models.CharField(max_length=100)
    delegation = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    telephone = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="Téléphone")
    email = models.EmailField(blank=True, null=True,
                              verbose_name="Email de Contact")
    position = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Position")

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        # Assurez-vous que le nom de l'URL est correct
        return reverse('entreprise:entreprise_prospection_detail', kwargs={'pk': self.pk})


# --- NOUVEAU MODÈLE TUTEUR DANS L'APPLICATION ENTREPRISES ---
class TuteurEntreprise(models.Model):
    """Représente l'employé désigné par l'entreprise pour encadrer un apprenti."""
    nom = models.CharField(max_length=100, verbose_name="Nom")
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    fonction = models.CharField(
        max_length=100, verbose_name="Fonction dans l'Entreprise")
    Matricule = models.CharField(
        max_length=50, verbose_name="Matricule", null=True, blank=True)
    date_integration = models.DateField(
        verbose_name="Date d'Intégration", null=True, blank=True)
    telephone = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="Téléphone")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")

    # Une entreprise peut avoir plusieurs tuteurs
    entreprise = models.ForeignKey(
        Entreprise,
        on_delete=models.CASCADE,
        verbose_name="Entreprise d'Apprentissage",
        related_name="tuteurs_entreprise"
    )

    class Meta:
        verbose_name = "Tuteur d'Entreprise"
        verbose_name_plural = "Tuteurs d'Entreprise"

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.entreprise.nom})"


class SuiviProspection(models.Model):
    # Choix d'état
    ETAT_CHOICES = [
        ('A_CONTACTER', 'À Contacter'),
        ('CONTACT_FAIT', 'Contact Fait'),
        ('RENDEZ_VOUS', 'Rendez-vous Planifié'),
        ('QUALIFIE', 'Qualifiée'),
        ('PERDU', 'Perdue'),
    ]

    entreprise = models.ForeignKey(
        Entreprise,
        on_delete=models.CASCADE,
        related_name='prospections',
        verbose_name="Entreprise Ciblée"
    )
    date_suivi = models.DateField(
        auto_now_add=True,
        verbose_name="Date du Suivi"
    )
    etat = models.CharField(
        max_length=50,
        choices=ETAT_CHOICES,
        default='A_CONTACTER',
        verbose_name="État de la Prospection"
    )
    notes = models.TextField(
        blank=True,
        null=True,
        verbose_name="Notes de Suivi"
    )
    # Exemple d'attribution à un commercial, ajustez l'importation si nécessaire
    # commercial = models.ForeignKey(
    #     'personnel.Personnel',
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    #     verbose_name="Commercial Attribué"
    # )

    class Meta:
        verbose_name = "Suivi de Prospection"
        verbose_name_plural = "Suivis de Prospection"
        ordering = ['-date_suivi']

    def __str__(self):
        return f"Prospection {self.etat} pour {self.entreprise.nom} le {self.date_suivi}"
