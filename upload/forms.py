from django import forms

from upload.models import Image

class ImageForm(forms.ModelForm):
    
    class Meta:
        model = Image
        fields = ("project","title","image",)
