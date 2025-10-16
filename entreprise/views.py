from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from .models import Entreprise, TuteurEntreprise


# -------- Entrteprise CRUD Views --------#
# ----------------------------------------------
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
    fields = ['nom', 'adresse', 'secteur_activite',
              'delegation', 'contact', 'position']  # Champs du formulaire
    template_name = 'entreprise/entreprise_form.html'
    # Où rediriger après succès
    success_url = reverse_lazy('entreprise:liste_entreprises')

# === 4. UPDATE ===


class EntrepriseUpdateView(UpdateView):
    """Permet de modifier une entreprise existante."""
    model = Entreprise
    fields = ['nom', 'adresse', 'secteur_activite',
              'delegation', 'contact', 'position']
    template_name = 'entreprise/entreprise_form.html'
    success_url = reverse_lazy('entreprise:liste_entreprises')

# === 5. DELETE ===


class EntrepriseDeleteView(DeleteView):
    """Permet de supprimer une entreprise."""
    model = Entreprise
    template_name = 'entreprise/entreprise_confirm_delete.html'
    success_url = reverse_lazy('entreprise:liste_entreprises')


# --- Vues pour le modèle TuteurEntreprise ---
# ----------------------------------------------
# -----------------------------------------------

# === 1. READ (Liste) ===
class TuteurEntrepriseListView(ListView):
    """Affiche la liste de tous les tuteurs d'entreprise."""
    model = TuteurEntreprise
    template_name = 'entreprise/tuteur_list.html'
    context_object_name = 'tuteurs'
    ordering = ['nom']

# === 2. READ (Détail) ===


class TuteurEntrepriseDetailView(DetailView):
    """Affiche les détails d'un Tuteur spécifique."""
    model = TuteurEntreprise
    template_name = 'entreprise/tuteur_detail.html'
    context_object_name = 'tuteur'

# === 3. CREATE ===


class TuteurEntrepriseCreateView(CreateView):
    """Permet de créer un nouveau tuteur d'entreprise."""
    model = TuteurEntreprise
    fields = ['nom', 'prenom', 'fonction', 'Matricule',
              'date_integration', 'telephone', 'email', 'entreprise']
    template_name = 'entreprise/tuteur_form.html'
    success_url = reverse_lazy('entreprise:liste_tuteurs')

# === 4. UPDATE ===


class TuteurEntrepriseUpdateView(UpdateView):
    """Permet de modifier un tuteur d'entreprise existant."""
    model = TuteurEntreprise
    fields = ['nom', 'prenom', 'fonction', 'Matricule',
              'date_integration', 'telephone', 'email', 'entreprise']
    template_name = 'entreprise/tuteur_form.html'
    success_url = reverse_lazy('entreprise:liste_tuteurs')

# === 5. DELETE ===


class TuteurEntrepriseDeleteView(DeleteView):
    """Permet de supprimer un tuteur d'entreprise."""
    model = TuteurEntreprise
    template_name = 'entreprise/tuteur_confirm_delete.html'
    success_url = reverse_lazy('entreprise:liste_tuteurs')
