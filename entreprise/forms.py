
from django import forms
from .models import SuiviProspection


class SuiviProspectionForm(forms.ModelForm):
    class Meta:
        model = SuiviProspection
        # Exclure l'entreprise, elle sera définie dans la vue POST
        fields = ['etat', 'notes']
        widgets = {
            'etat': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Détails du contact, prochaines étapes, etc.'}),
        }
