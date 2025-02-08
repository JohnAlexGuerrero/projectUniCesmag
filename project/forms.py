from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from project.models import Project

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
