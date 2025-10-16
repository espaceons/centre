
from django.views.generic import TemplateView

from entreprise.models import Entreprise, TuteurEntreprise
from mission.models import Visite
from personnel.models import Personnel

# === 0. Accueil ===


class AccueilView(TemplateView):
    """Affiche la page d'accueil."""
    template_name = 'accueil.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Récupération des décomptes
        context['total_personnel'] = Personnel.objects.count()
        context['total_entreprises'] = Entreprise.objects.count()
        context['total_missions'] = Visite.objects.count()
        context['total_tuteurs'] = TuteurEntreprise.objects.count()

        # Optionnel : Récupération des 5 dernières missions pour l'affichage
        context['dernieres_missions'] = Visite.objects.all().order_by(
            '-date_depart')[:5]

        return context
