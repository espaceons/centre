from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy

from mission.models import Visite
from .models import Personnel


# =======================================================
# VUES CRUD POUR LE PERSONNEL
# =======================================================


class PersonnelListView(ListView):
    model = Personnel
    template_name = 'personnel/personnel_list.html'
    context_object_name = 'personnels'


class PersonnelDetailView(DetailView):
    model = Personnel
    template_name = 'personnel/personnel_detail.html'


class PersonnelCreateView(CreateView):
    """Permet de créer une nouvelle entreprise."""
    model = Personnel
    fields = ['prenom', 'nom', 'fonction',
              'iu']  # Champs du formulaire
    template_name = 'personnel/personnel_form.html'
    # Où rediriger après succès
    success_url = reverse_lazy('personnel:liste_personnels')


class PersonnelUpdateView(UpdateView):
    model = Personnel
    # Incluez les champs directs ET la relation M2M pour la modifier si nécessaire
    fields = ['prenom', 'nom', 'fonction',
              'iu', 'entreprises_visitees']
    template_name = 'personnel/personnel_form.html'
    success_url = reverse_lazy('personnel:liste_personnels')


class PersonnelDeleteView(DeleteView):
    model = Personnel
    template_name = 'personnel/personnel_confirm_delete.html'
    success_url = reverse_lazy('personnel:liste_personnels')


# =======================================================
# VUES CRUD POUR LES VISITES (Relation N:N)
# =======================================================

class VisiteCreateView(CreateView):
    model = Visite
    # Le champ 'entreprise' sera un choix parmi les Entreprises disponibles
    fields = ['personnel', 'entreprise', 'date_visite', 'objet', 'rapport']
    template_name = 'mission/visite_form.html'

    def get_initial(self):
        initial = super().get_initial()
        personnel_pk = self.kwargs.get('personnel_pk')
        if personnel_pk:
            initial['personnel'] = personnel_pk
        return initial

    # Rediriger vers la page du personnel après la création
    def get_success_url(self):
        # self.object est la visite en cours de création/modification
        return reverse_lazy('personnel:detail_personnel', kwargs={'pk': self.object.personnel.pk})


class VisiteUpdateView(UpdateView):
    model = Visite
    fields = ['personnel', 'entreprise', 'date_visite',
              'objet', 'rapport']
    template_name = 'mission/visite_form.html'

    # Rediriger vers la page du personnel après la modification
    def get_success_url(self):
        # self.object est la visite en cours de création/modification
        return reverse_lazy('personnel:detail_personnel', kwargs={'pk': self.object.personnel.pk})


class VisiteDeleteView(DeleteView):
    model = Visite
    template_name = 'personnel/visite_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('personnel:detail_personnel', kwargs={'pk': self.object.personnel.pk})


class OrdreMissionView(DetailView):
    """Affiche les détails d'une visite dans un format simple pour impression (Ordre de Mission)."""
    model = Visite
    template_name = 'personnel/ordre_mission.html'
    context_object_name = 'visite'
