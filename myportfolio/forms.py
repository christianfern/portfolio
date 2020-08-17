from django import forms
from django.core.exceptions import ValidationError

class DefinitionLookupForm(forms.Form):
    word = forms.CharField(max_length = 100)