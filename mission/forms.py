from django import forms
from .models import Visite


class VisiteForm(forms.ModelForm):
    """
    Formulaire pour créer et modifier les enregistrements de mission (Visite).
    Utilise le widget DateTimeInput avec type='datetime-local' pour afficher 
    un calendrier de sélection de date et d'heure.
    """
    class Meta:
        model = Visite
        fields = [
            'personnel',
            'entreprise',
            'date_depart',
            'date_retour',
            'lieu',
            'type_mission',
            'moyen_transport',
            'objet',
            'rapport',
            'etat',
        ]

        # Widgets pour garantir l'affichage d'un calendrier HTML5 (date et heure)
        widgets = {
            # Utilisation de 'datetime-local' pour le calendrier date/heure
            'date_depart': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'}
            ),
            'date_retour': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'}
            ),
            # Ajout explicite de form-control aux autres widgets pour plus de robustesse
            'personnel': forms.Select(attrs={'class': 'form-control'}),
            'entreprise': forms.Select(attrs={'class': 'form-control'}),
            'lieu': forms.TextInput(attrs={'class': 'form-control'}),
            'type_mission': forms.TextInput(attrs={'class': 'form-control'}),
            'moyen_transport': forms.TextInput(attrs={'class': 'form-control'}),
            'objet': forms.TextInput(attrs={'class': 'form-control'}),
            'rapport': forms.Textarea(attrs={'class': 'form-control'}),
            'etat': forms.Select(attrs={'class': 'form-control'}),
        }
