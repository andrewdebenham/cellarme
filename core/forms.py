from django import forms
from .models import Wine

class WineForm(forms.ModelForm):
    class Meta:
        model = Wine
        fields = ['producer', 'variety', 'year', 'style', 'country', 'region', 'storage_date', 'months_for_storage']
        widgets = {
            'storage_date': forms.DateInput(
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }