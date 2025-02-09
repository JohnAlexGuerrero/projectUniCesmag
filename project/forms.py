from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from project.models import Project, Categorization

class ProjectForm(forms.ModelForm):
    # description = forms.CharField(widget=CKEditor5Widget)
    
    class Meta:
        model = Project
        fields = ("title","description","version")
        
        widgets = {
            "description": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            )
        }


class CategorizationForm(forms.ModelForm):
    
    class Meta:
        model = Categorization
        fields = ("project","license","software","sector","category")
        
        widgets = {
            "project": forms.TextInput(attrs={}),
            "software": forms.Select(attrs={'class':'form-select form-select-sm'}),
            "license": forms.RadioSelect(attrs={'class':'form-ckeck-input'}),
            "category": forms.RadioSelect(attrs={'class':'form-ckeck-input'}),
            "sector": forms.Select(attrs={
                'class':'form-select form-select-sm js-example-basic-single',
            })
        }
