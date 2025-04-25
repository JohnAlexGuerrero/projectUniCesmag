from django import forms
# from django_ckeditor_5.widgets import CKEditor5Widget

from project.models import Project, Categorization

class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ("user","name","title")
        
        widgets = {
            "name": forms.TextInput(attrs={
                'class':'form-control p-3',
                'style': 'border-bottom: 3px solid rgb(89, 89, 228); font-size:30px; font-weight:bold; color:rgb(89, 89, 228);',
                'placeholder':"Ingresa el nombre de tu software",
                'autocomplete':"off" 
            }),
            
            "title": forms.Textarea(attrs={
                'class':'form-control p-3',
                "rows":"3", 
                "cols":"3",
                "style":"border-bottom: 3px solid rgb(89, 89, 228); font-size:20px; font-weight:bold; color:rgb(89, 89, 228);",
                "placeholder":"Ingresa el nombre general de tu software",
                "autocomplete":"off"
            }),
            
        }


class CategorizationForm(forms.ModelForm):
    
    class Meta:
        model = Categorization
        fields = ("project","license","software","sector","category")
        
        widgets = {
            "project": forms.TextInput(attrs={}),
            "software": forms.RadioSelect(attrs={'class':'form-ckeck-input'}),
            "license": forms.RadioSelect(attrs={'class':'form-ckeck-input'}),
            "category": forms.RadioSelect(attrs={'class':'form-ckeck-input'}),
            "sector": forms.Select(attrs={
                'class':'form-select form-select-sm js-example-basic-single',
            })
        }
