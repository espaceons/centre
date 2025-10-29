from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy

from mission.models import Visite
from .models import Personnel

from django.shortcuts import render, get_object_or_404


# =======================================================
# VUES CRUD POUR LE PERSONNEL
# =======================================================


class PersonnelListView(ListView):
    model = Personnel
    template_name = 'personnel/personnel_list.html'
    context_object_name = 'personnels'


# def detail_personnel(request, pk):
#     """
#     Affiche le détail d'un membre du personnel et prépare le contexte
#     pour afficher le nombre de missions par entreprise.
#     """
#     # 1. Récupération du Personnel
#     personnel = get_object_or_404(Personnel, pk=pk)

#     # 2. Récupérer les entreprises distinctes visitées par ce personnel
#     # On utilise la relation ManyToMany 'entreprises_visitees'
#     entreprises_visitees = personnel.entreprises_visitees.all().distinct()

#     # -----------------------------------------------------------------------------------------------
#     #    ('ANNULEE', 'Annulée'),  ('NON_REALISER', 'Non Realiser'),
#     # 3. Logique clé : Calculer et injecter le nombre de missions pour chaque entreprise, par état.
#     # Nous supposons que les valeurs des états sont : 'PLANNIFIEE', 'EN_COUR', 'REALISEE'
#     for entreprise in entreprises_visitees:
#         # A. Compteur Plannifié (Badge Bleu/Info)
#         count_planifiee = entreprise.visite_set.filter(
#             personnel=personnel,
#             etat='PLANNIFIEE'
#         ).count()

#         # B. Compteur En cours (Badge Jaune/Warning)
#         count_en_cours = entreprise.visite_set.filter(
#             personnel=personnel,
#             etat='EN_COUR'
#         ).count()

#         # C. Compteur Réalisé (Badge Vert/Success)
#         count_realisee = entreprise.visite_set.filter(
#             personnel=personnel,
#             etat='REALISEE'
#         ).count()
#         # D. Compteur Annulée (Badge Vert/Success)
#         count_annulee = entreprise.visite_set.filter(
#             personnel=personnel,
#             etat='ANNULEE'
#         ).count()
#         # E. Compteur Non Réalisé (Badge Vert/Success)
#         count_non_realisee = entreprise.visite_set.filter(
#             personnel=personnel,
#             etat='NON_REALISER'
#         ).count()

#         # Injection des résultats dans l'objet entreprise (temporairement pour le template)
#         entreprise.count_planifiee = count_planifiee
#         entreprise.count_en_cours = count_en_cours
#         entreprise.count_realisee = count_realisee
#         entreprise.count_annulee = count_annulee
#         entreprise.count_non_realisee = count_non_realisee

#         # Le compte total est toujours calculé mais n'est plus la priorité d'affichage
#         entreprise.mission_count = count_planifiee + count_en_cours + \
#             count_realisee + count_annulee + count_non_realisee

#     context = {
#         'personnel': personnel,
#         # On passe explicitement la liste enrichie au template
#         'entreprises_visitees_enrichies': entreprises_visitees
#     }

#     return render(request, 'personnel/personnel_detail.html', context)
# =======================================================
def detail_personnel(request, pk):
    """
    Affiche le détail d'un membre du personnel et prépare le contexte
    pour afficher le nombre de missions par entreprise et les statistiques globales.
    """
    # 1. Récupération du Personnel
    personnel = get_object_or_404(Personnel, pk=pk)

    # 2. Statistiques Globales des Missions du Personnel
    missions_du_personnel = Visite.objects.filter(personnel=personnel)

    total_missions = missions_du_personnel.count()
    missions_planifiees = missions_du_personnel.filter(
        etat='PLANNIFIEE').count()
    missions_en_cours = missions_du_personnel.filter(etat='EN_COURS').count()
    missions_realisees = missions_du_personnel.filter(etat='REALISE').count()
    missions_annulees = missions_du_personnel.filter(etat='ANNULEE').count()
    missions_non_realisees = missions_du_personnel.filter(
        etat='NON_REALISER').count()

    # 3. Récupérer les entreprises distinctes visitées par ce personnel
    # On utilise la relation ManyToMany 'entreprises_visitees' (via Visite)
    # Note: On s'assure que le champ `etat` de Visite correspond bien aux valeurs de votre modèle.
    # Les états utilisés sont: 'PLANNIFIEE', 'EN_COURS', 'REALISE', 'ANNULEE', 'NON_REALISER'
    entreprises_visitees = personnel.entreprises_visitees.all().distinct()

    # 4. Logique clé : Calculer et injecter le nombre de missions pour chaque entreprise, par état.
    # Nouvelle liste pour stocker les entreprises enrichies
    entreprises_visitees_list = []

    for entreprise in entreprises_visitees:
        # Filtrer les missions pour cette entreprise spécifique et ce personnel
        missions_entreprise = missions_du_personnel.filter(
            entreprise=entreprise)

        # A. Compteur Plannifié
        count_planifiee = missions_entreprise.filter(etat='PLANNIFIEE').count()

        # B. Compteur En cours
        # ATTENTION: Votre code original utilisait 'EN_COUR', l'ancienne version utilisait 'EN_COURS'.
        # J'utilise 'EN_COURS' pour être cohérent avec l'ancienne DetailView.
        count_en_cours = missions_entreprise.filter(etat='EN_COURS').count()

        # C. Compteur Réalisé
        # ATTENTION: Votre code original utilisait 'REALISEE', l'ancienne version utilisait 'REALISE'.
        # J'utilise 'REALISE' pour être cohérent avec l'ancienne DetailView.
        count_realisee = missions_entreprise.filter(etat='REALISE').count()

        # D. Compteur Annulée
        count_annulee = missions_entreprise.filter(etat='ANNULEE').count()

        # E. Compteur Non Réalisé
        count_non_realisee = missions_entreprise.filter(
            etat='NON_REALISER').count()

        # Construction de l'objet de contexte (similaire à la DetailView)
        entreprises_visitees_list.append({
            'entreprise': entreprise,
            'total_missions': missions_entreprise.count(),  # Total pour cette entreprise
            'planifiees': count_planifiee,
            'en_cours': count_en_cours,
            'realisees': count_realisee,
            'annulees': count_annulee,
            'non_realisees': count_non_realisee,
            'derniere_visite': missions_entreprise.order_by('-date_depart').first()
        })

    # 5. Création du contexte final
    context = {
        'personnel': personnel,
        # Statistiques globales
        'total_missions': total_missions,
        'missions_planifiees': missions_planifiees,
        'missions_en_cours': missions_en_cours,
        'missions_realisees': missions_realisees,
        'missions_annulees': missions_annulees,
        'missions_non_realisees': missions_non_realisees,

        # Liste des entreprises enrichies pour le tableau du bas
        'entreprises_visitees_list': entreprises_visitees_list
    }

    return render(request, 'personnel/personnel_detail.html', context)
# =======================================================


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
