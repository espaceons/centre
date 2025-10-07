from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from .models import Entreprise

# === 1. READ (Liste) ===


class EntrepriseListView(ListView):
    """Affiche la liste de toutes les entreprises."""
    model = Entreprise
    template_name = 'entreprise/entreprise_list.html'  # Chemin du template
    # Nom de la variable utilisée dans le template
    context_object_name = 'entreprises'

# === 2. READ (Détail) ===


class EntrepriseDetailView(DetailView):
    """Affiche les détails d'une entreprise spécifique."""
    model = Entreprise
    template_name = 'entreprise/entreprise_detail.html'

# === 3. CREATE ===


class EntrepriseCreateView(CreateView):
    """Permet de créer une nouvelle entreprise."""
    model = Entreprise
    fields = ['nom', 'adresse', 'secteur_activite']  # Champs du formulaire
    template_name = 'entreprise/entreprise_form.html'
    # Où rediriger après succès
    success_url = reverse_lazy('entreprise:liste_entreprises')

# === 4. UPDATE ===


class EntrepriseUpdateView(UpdateView):
    """Permet de modifier une entreprise existante."""
    model = Entreprise
    fields = ['nom', 'adresse', 'secteur_activite']
    template_name = 'entreprise/entreprise_form.html'
    success_url = reverse_lazy('entreprise:liste_entreprises')

# === 5. DELETE ===


class EntrepriseDeleteView(DeleteView):
    """Permet de supprimer une entreprise."""
    model = Entreprise
    template_name = 'entreprise/entreprise_confirm_delete.html'
    success_url = reverse_lazy('entreprise:liste_entreprises')
