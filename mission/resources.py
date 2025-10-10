from mission.models import Visite
from personnel.models import Personnel
from entreprise.models import Entreprise
from import_export import resources
from import_export.fields import Field


class VisiteResource(resources.ModelResource):
    """
    Définit comment importer et exporter le modèle Visite.
    Nous utilisons les IDs pour lier Personnel et Entreprise.
    """

    # Champ personnalisé pour Personnel
    # On suppose que l'utilisateur fournira le nom complet (prenom nom) ou l'ID
    # Pour l'exemple, nous allons utiliser l'ID (pk) pour une correspondance fiable.
    personnel_id = Field(
        column_name='personnel',
        attribute='personnel',
        widget=None  # Optionnel, on le laisse vide ici
    )

    # Champ personnalisé pour Entreprise
    entreprise_id = Field(
        column_name='entreprise',
        attribute='entreprise',
        widget=None  # Optionnel
    )

    class Meta:
        model = Visite
        # Champs que nous voulons mapper directement :
        fields = (
            'id',
            'date_depart',
            'date_retour',
            'objet',
            'rapport',
        )
        # Champs en lecture seule (importés mais non modifiables)
        # On exclut les champs qui ne sont plus utilisés, si vous le souhaitez
        skip_unchanged = True
        report_skipped = False

    # Méthode pour lier l'ID du Personnel au modèle réel
    def before_import_row(self, row, **kwargs):
        # Assurez-vous que l'application "personnel" est installée et que le modèle Personnel est importé.

        # 1. Traitement du Personnel
        personnel_pk = row.get('personnel')
        if personnel_pk:
            try:
                # Utiliser l'ID du personnel pour trouver l'objet
                personnel_instance = Personnel.objects.get(pk=personnel_pk)
                # Remplace la PK par l'instance du modèle
                row['personnel'] = personnel_instance
            except Personnel.DoesNotExist:
                raise Exception(
                    f"Personnel avec ID {personnel_pk} non trouvé.")
        else:
            raise Exception("L'ID du personnel est requis pour l'importation.")

        # 2. Traitement de l'Entreprise
        entreprise_pk = row.get('entreprise')
        if entreprise_pk:
            try:
                # Utiliser l'ID de l'entreprise pour trouver l'objet
                entreprise_instance = Entreprise.objects.get(pk=entreprise_pk)
                # Remplace la PK par l'instance du modèle
                row['entreprise'] = entreprise_instance
            except Entreprise.DoesNotExist:
                # Assurez-vous que l'application "entreprise" est installée et que le modèle Entreprise est importé.
                raise Exception(
                    f"Entreprise avec ID {entreprise_pk} non trouvée.")
        else:
            raise Exception(
                "L'ID de l'entreprise est requis pour l'importation.")

        return row
