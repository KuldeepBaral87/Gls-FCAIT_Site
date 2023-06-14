from django import forms
from .models import Menumaster,Submenu,Coursemaster
 
class menuform(forms.ModelForm):
    class Meta:
        model=Menumaster
        fields="__all__"

class submenuform(forms.ModelForm):
    class Meta:
        model=Submenu
        fields="__all__"

class coursemenuform(forms.ModelForm):
    class Meta:
        model=Coursemaster
        fields="__all__"