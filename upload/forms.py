from django import forms 
from .models import *
  
class GalleryForm(forms.ModelForm): 
  
    class Meta: 
        model = Gallery 
        fields = ['name', 'image','category']