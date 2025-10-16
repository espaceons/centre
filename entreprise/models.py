from django.db import models

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
