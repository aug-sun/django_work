from django import forms
from dal import autocomplete
from birix.models import *

class ContragentsForm(forms.ModelForm):
    class Meta:
        model = Contragents
        fields = 'ca_name'
        widgets = {
                'ca_name': autocomplete.ModelSelect2(url='contragents-autocomplete')
        }
