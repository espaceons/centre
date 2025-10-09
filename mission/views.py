from django.views.generic import CreateView, UpdateView, ListView
from django.urls import reverse_lazy
from .models import Visite
# Assurez-vous d'importer les modèles nécessaires (si non définis dans mission)
# Si vous prévoyez de pré-remplir le personnel, vous devrez peut-être importer :
# from personnel.models import Personnel
# from django.shortcuts import get_object_or_404

# ====================================================================
# VUE DE CRÉATION : Pour enregistrer une nouvelle mission (visite)
# ====================================================================


class VisiteCreateView(CreateView):
    """
    Vue pour la création d'un nouvel enregistrement de mission (Visite).
    Utilise les champs 'date_depart' et 'date_retour' pour la planification.
    """
    model = Visite
    # Liste des champs à afficher dans le formulaire
    fields = [
        'personnel',
        'entreprise',
        'date_depart',
        'date_retour',
        'objet',
        'rapport'
    ]
    template_name = 'mission/visite_form.html'

    def get_success_url(self):
        """Redirige vers la page détaillée du personnel après la création."""
        # self.object est l'instance de Visite nouvellement créée
        return reverse_lazy('personnel:detail_personnel', kwargs={'pk': self.object.personnel.pk})

    def get_initial(self):
        """Permet de pré-remplir le champ 'personnel' si l'ID est passé dans l'URL."""
        initial = super().get_initial()
        # Récupère 'personnel_pk' si l'URL /missions/personnel/<int:personnel_pk>/creer/ est utilisée
        personnel_pk = self.kwargs.get('personnel_pk')
        if personnel_pk:
            initial['personnel'] = personnel_pk
        return initial


# ====================================================================
# VUE DE MODIFICATION : Pour mettre à jour une mission existante
# ====================================================================
class VisiteUpdateView(UpdateView):
    """
    Vue pour la modification d'un enregistrement de mission (Visite) existant.
    """
    model = Visite
    # Utilise les mêmes champs que la vue de création
    fields = [
        'personnel',
        'entreprise',
        'date_depart',
        'date_retour',
        'objet',
        'rapport'
    ]
    template_name = 'mission/visite_form.html'

    def get_success_url(self):
        """Redirige vers la page détaillée du personnel après la modification."""
        # self.object est l'instance de Visite modifiée
        return reverse_lazy('personnel:detail_personnel', kwargs={'pk': self.object.personnel.pk})


# ====================================================================
# NOUVELLE VUE DE LISTE : Pour afficher toutes les missions
# ====================================================================
class VisiteListView(ListView):
    """
    Affiche la liste de toutes les missions enregistrées.
    Par défaut, le contexte est nommé 'visite_list'.
    """
    model = Visite
    template_name = 'mission/visite_list.html'
    context_object_name = 'missions'  # Renommer le contexte pour plus de clarté
    # L'ordre est déjà défini dans le modèle : ['-date_depart']
