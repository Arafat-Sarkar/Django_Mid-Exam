from django import forms
from .import models

class CarForm(forms.ModelForm):
    class Meta:
         model = models.carmodel
         fields = '__all__'


class CommentForm (forms.ModelForm):
    class Meta:
         model = models.Comment
         fields = ['name', 'email', 'body']