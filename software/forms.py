from django import forms

from software.models import Objective, App, Requeriment
from author.models import Participant

from django_ckeditor_5.widgets import CKEditor5Widget

from datetime import datetime

class ObjectiveForm(forms.ModelForm):
    authors = forms.ModelMultipleChoiceField(queryset=Participant.objects.all(), widget=forms.CheckboxSelectMultiple())
    
    class Meta:
        model = Objective
        fields = ("objectiveId","title","version","authors","fuente","description","importancia","urgencia","status","estabilidad","comments","software")

        widgets = {
            "objectiveId": forms.TextInput(attrs={'class':"form-control", 'style':"width:100px;"}),
            "title": forms.TextInput(attrs={'class':"form-control", 'placeholder':"Ingrese el título del objetivo"}),
            "version": forms.TextInput(attrs={'class':"form-control", 'placeholder':"Ingrese la versión del objetivo"}),
            "fuente": forms.TextInput(attrs={'class':"form-control", 'placeholder':"Ingrese la fuente del objetivo"}),
            "description": forms.Textarea(attrs={'class':"form-control", 'rows':'3', 'placeholder':"Ingrese la descripción del objetivo"}),
            "comments": forms.Textarea(attrs={'class':"form-control", 'rows':'3', 'placeholder':"Ingrese comentarios adicionales"}),
            #"authors": forms.CheckboxSelectMultiple(attrs={'class':''}),
            "importancia": forms.RadioSelect(attrs={'class':'form-check-input'}),
            "urgencia": forms.RadioSelect(attrs={'class':'form-check-input'}),
            "status": forms.RadioSelect(attrs={'class':'form-check-input'}),
            "estabilidad": forms.RadioSelect(attrs={'class':'form-check-input'}),
        }
        
    def __init__(self, *args, project__id=None,software__id=None, **kwargs):
        super().__init__(*args, **kwargs)
        if project__id is not None:
            self.fields['authors'].queryset = Participant.objects.filter(project__id=project__id)
        else:
            self.fields['authors'].queryset = Participant.objects.all()
        
        self.fields['version'].initial = f'1.0 ({datetime.now().strftime("%d/%m/%Y")})'
        
        if software__id is not None:
            count_objectives = Objective.objects.filter(software__id=software__id).count()
            self.fields['objectiveId'].initial = f'OBJ-0{count_objectives + 1}' if count_objectives < 10 else f'OBJ-{count_objectives + 1}'
 
        
class RequerimentForm(forms.ModelForm):
    authors = forms.ModelMultipleChoiceField(queryset=Participant.objects.none(), widget=forms.CheckboxSelectMultiple())
    
    class Meta:
        model = Requeriment
        fields = ("title","version","authors","fuente","description","importancia","urgencia","status","estabilidad","comments","software")

        widgets = {
            "title": forms.TextInput(attrs={'class':"form-control", 'placeholder':"Ingrese el título del requisito"}),
            "version": forms.TextInput(attrs={'class':"form-control", 'placeholder':"Ingrese la versión del requisito"}),
            "fuente": forms.TextInput(attrs={'class':"form-control", 'placeholder':"Ingrese la fuente del requisito"}),
            "description": forms.Textarea(attrs={'class':"form-control", 'rows':'3', 'placeholder':"Ingrese la descripción del requisito"}),
            "comments": forms.Textarea(attrs={'class':"form-control", 'rows':'3', 'placeholder':"Ingrese comentarios adicionales"}),
            "authors": forms.CheckboxSelectMultiple(attrs={'class':''}),
            "importancia": forms.RadioSelect(attrs={'class':'form-check-input'}),
            "urgencia": forms.RadioSelect(attrs={'class':'form-check-input'}),
            "status": forms.RadioSelect(attrs={'class':'form-check-input'}),
            "estabilidad": forms.RadioSelect(attrs={'class':'form-check-input'}),
        }
        
    def __init__(self, *args, project__id=None, **kwargs):
        super().__init__(*args, **kwargs)
        if project__id is not None:
            self.fields['authors'].queryset = Participant.objects.filter(project__id=project__id)
        else:
            self.fields['authors'].queryset = Participant.objects.none()
        
class AppDescriptionForm(forms.ModelForm):
    
    class Meta:
        model = App
        fields = ("description",)
        
        widgets = {
            "description": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            )
        }
