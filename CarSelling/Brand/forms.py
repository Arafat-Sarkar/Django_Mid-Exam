from django import forms
from .import models

class BrandModel(forms.ModelForm):
    class Meta:
        model = models.brandmodel
        fields = '__all__'