from django import forms


class TechnologiesForm(forms.Form):
    technology_name = forms.CharField(max_length=128)
