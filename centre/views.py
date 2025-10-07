
from django.views.generic import TemplateView

# === 0. Accueil ===


class AccueilView(TemplateView):
    """Affiche la page d'accueil."""
    template_name = 'accueil.html'
