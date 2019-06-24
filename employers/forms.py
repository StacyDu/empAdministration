from django import forms
from employers.models import (
    Developers,
    Technologies,
)


class TechnologiesForm(forms.ModelForm):
    # Allows customizing any field even within Meta class
    required_css_class = "required"
    technology_name = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'placeholder': 'Ex.: Python'}))

    class Meta:
        model = Technologies
        fields = [
            'technology_name',
        ]


class DevelopersForm(forms.ModelForm):
    date_hired = forms.DateField(widget=forms.SelectDateWidget)
    middle_name = forms.CharField(required=False)

    class Meta:
        model = Developers
        fields = '__all__'

        widgets = {
            'technology': forms.CheckboxSelectMultiple(),
        }

