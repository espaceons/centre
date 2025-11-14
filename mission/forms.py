from django import forms

from entreprise.models import Entreprise
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
                attrs={'type': 'text', 'class': 'form-control datetimepicker'}
            ),
            'date_retour': forms.DateTimeInput(
                attrs={'type': 'text', 'class': 'form-control datetimepicker'}
            ),
            # Ajout explicite de form-control aux autres widgets pour plus de robustesse
            'personnel': forms.Select(attrs={'class': 'form-control'}),
            'entreprise': forms.Select(attrs={'class': 'form-control', 'id': 'id_entreprise'}),
            'lieu': forms.TextInput(attrs={'class': 'form-control'}),
            'type_mission': forms.TextInput(attrs={'class': 'form-control'}),
            'moyen_transport': forms.TextInput(attrs={'class': 'form-control'}),
            'objet': forms.TextInput(attrs={'class': 'form-control'}),
            'rapport': forms.Textarea(attrs={'class': 'form-control'}),
            'etat': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 1. Récupérer l'ID du personnel s'il est initialisé (pour le mode édition ou pré-remplissage)
        personnel_id = None
        if self.instance.pk:
            personnel_id = self.instance.personnel_id
        elif 'initial' in kwargs and 'personnel' in kwargs['initial']:
            personnel_id = kwargs['initial']['personnel']

        # 2. Filtrer le champ 'entreprise'
        if personnel_id:
            # Récupérer les ID des entreprises associées à ce personnel
            # Basé sur les missions existantes :
            entreprises_ids = Visite.objects.filter(
                personnel_id=personnel_id
            ).values_list('entreprise_id', flat=True).distinct()

            # Filtrer le QuerySet des entreprises
            self.fields['entreprise'].queryset = Entreprise.objects.filter(
                id__in=entreprises_ids
            ).order_by('nom')
        else:
            # Si aucun personnel n'est sélectionné initialement, on vide la liste
            self.fields['entreprise'].queryset = Entreprise.objects.none()
