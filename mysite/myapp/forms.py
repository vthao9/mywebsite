from django import forms
from django.core.validators import validate_slug

def must_be_caps(value):
    if not value.isupper():
        raise forms.ValidationError("Need to be all uppercase")

    return value

class SuggestionForm(forms.Form):
    suggestion_field = forms.CharField(label='Suggestion', max_length=240)
