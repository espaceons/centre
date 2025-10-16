from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Visite


@admin.register(Visite)
class VisiteAdmin(ImportExportModelAdmin):
    """
    Configure la page d'administration de Visite pour permettre 
    l'importation et l'exportation.
    """
    resource_class = Visite  # Classe ressource pour import-export

    # Affichage des champs dans la liste d'administration
    list_display = (
        'personnel',
        'entreprise',
        'date_depart',
        'etat',  # <-- NOUVEAU CHAMP AJOUTÉ
        'objet',
        'rapport'
    )

    # Permettre la recherche
    search_fields = ('personnel__nom', 'entreprise__nom', 'objet')

    # Filtres
    list_filter = ('date_depart', 'personnel', 'entreprise',
                   'etat')  # <-- NOUVEAU FILTRE AJOUTÉ
