from import_export import resources
from .models import Entreprise  # Assurez-vous que l'importation est correcte


class EntrepriseResource(resources.ModelResource):
    """
    Définit comment importer et exporter le modèle Entreprise.
    """
    class Meta:
        model = Entreprise
        # Liste des champs que vous souhaitez importer/exporter
        fields = (
            'id',
            'nom',
            'adresse',
            'secteur_activite',
            'delegation',
            'contact',
            # Ajoutez ici tous les autres champs de votre modèle Entreprise
        )
        # Permet de sauter les lignes non modifiées et de rapporter les lignes ignorées
        skip_unchanged = True
        report_skipped = True
        # Facultatif : utiliser les identifiants de champ au lieu des noms conviviaux pour l'en-tête
        # export_order = ('id', 'nom', 'adresse', 'contact')
