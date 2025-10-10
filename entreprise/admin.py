from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Entreprise  # Assurez-vous que l'importation est correcte
from .resources import EntrepriseResource


@admin.register(Entreprise)
class EntrepriseAdmin(ImportExportModelAdmin):
    """
    Configure la page d'administration de l'Entreprise pour permettre 
    l'importation et l'exportation.
    """
    resource_class = EntrepriseResource

    # Affichage des champs dans la liste d'administration
    list_display = (
        'id',
        'nom',
        'adresse',
        'secteur_activite',
        'delegation',
        'contact',
    )

    # Permettre la recherche sur le nom et le contact
    search_fields = ('nom', 'contact')

    # Filtres
    list_filter = ('nom',)
