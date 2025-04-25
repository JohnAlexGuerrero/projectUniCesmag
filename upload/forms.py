from django import forms

from upload.models import Image

class ImageForm(forms.ModelForm):
    
    class Meta:
        model = Image
        fields = ("project","title","image","is_logo")
        
        labels = {
            "title":("Titulo de la imagen"),
            "is_logo": ("logo?")    
        }
        
        widgets = {
            "project": forms.TextInput(attrs={'style':'display:none'}),
            "title": forms.TextInput(attrs={'class':'form-control p-1'}),
            "is_logo": forms.CheckboxInput(attrs={})
        }
