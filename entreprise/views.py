from .forms import SuiviProspectionForm
from .models import Entreprise, SuiviProspection
from django.views.generic import DetailView
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect
from django.views.generic.edit import SingleObjectMixin, FormMixin
from django.contrib import messages


from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse, reverse_lazy

from entreprise.forms import SuiviProspectionForm
from .models import Entreprise, SuiviProspection, TuteurEntreprise


from django.views.generic.edit import ProcessFormView

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


# ==== Prospection des entreprise ===

class ProspectionListeView(ListView):
    """Affiche la liste de tous les tuteurs d'entreprise."""
    model = Entreprise
    template_name = 'entreprise/detail_prospection.html'
    context_object_name = 'nom'
    ordering = ['nom']


# class EntrepriseProspectionDetailView(DetailView):
#     """
#     Affiche les détails d'une entreprise et la liste de ses suivis de prospection.
#     """
#     model = Entreprise
#     template_name = 'entreprise/detail_prospection.html'
#     context_object_name = 'entreprise'
#     # Utilise l'ID (pk) de l'entreprise dans l'URL pour la trouver

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # Récupère tous les objets SuiviProspection liés à cette entreprise
#         # Grâce au related_name='prospections' défini dans le modèle.
#         context['prospections_list'] = self.object.prospections.all()
    # return context

# Utiliser DetailView et ProcessFormView pour afficher le détail et gérer un formulaire


# Modification de la vue pour supporter le formulaire d'ajout
# <--- C'EST L'ORDRE CLASSIQUE QUI FONCTIONNE


class EntrepriseProspectionDetailView(DetailView):
    model = Entreprise
    template_name = "entreprise/detail_prospection.html"
    context_object_name = "entreprise"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        entreprise = self.get_object()

        # Form vide pour l’affichage
        context["form_suivi"] = SuiviProspectionForm()

        # Liste des suivis
        context["prospections_list"] = SuiviProspection.objects.filter(
            entreprise=entreprise
        ).order_by('-date_suivi')

        return context

    def post(self, request, *args, **kwargs):
        entreprise = self.get_object()
        form = SuiviProspectionForm(request.POST)

        if form.is_valid():
            suivi = form.save(commit=False)
            suivi.entreprise = entreprise
            suivi.save()

            return redirect(
                reverse('entreprise:entreprise_prospection_detail',
                        kwargs={'pk': entreprise.pk})
            )

        # Si le formulaire n'est pas valide → réafficher avec erreurs
        context = self.get_context_data()
        context["form_suivi"] = form

        return render(request, self.template_name, context)


class SupprimerProspectionView(DeleteView):
    model = SuiviProspection
    template_name = "entreprise/prospection_confirm_delete.html"

    def get_success_url(self):
        return self.object.entreprise.get_absolute_url()


class ModifierProspectionView(UpdateView):
    model = SuiviProspection
    form_class = SuiviProspectionForm
    template_name = "entreprise/modifier_prospection.html"
    context_object_name = "suivi"

    def form_valid(self, form):
        messages.success(
            self.request, "Le suivi de prospection a été modifié avec succès.")
        return super().form_valid(form)

    def get_success_url(self):
        # Retour automatique vers la page de prospection de l'entreprise
        return reverse_lazy(
            "entreprise:entreprise_prospection_detail",
            kwargs={"pk": self.object.entreprise.pk}
        )
