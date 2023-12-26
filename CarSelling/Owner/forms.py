from django import forms
from .import models

class OwnerForm(forms.ModelForm):
    class Meta:
         model = models.profileModel
         fields = '__all__'