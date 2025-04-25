from django import forms

from author.models import Organization, Participant

class OrganizationForm(forms.ModelForm):
    
    class Meta:
        model = Organization
        fields = ("project","name","address","phone","email","description",)
        
        labels = {
            "project": ("Proyecto"),
            "name": ("Nombre institución"),
            "address": ("Dirección"),
            "phone": ("Teléfono"),
            "email":("Correo electronico"),
            "description": ("Descripción (Opcional)")
        }
        
        widgets = {
            "project": forms.Select(attrs={
                'class':'form-select border-0',
                'style':''
            }),
            "name": forms.TextInput(attrs={
                'class':'form-control',
                'autocomplete':"off",
            }),
            "address": forms.TextInput(attrs={
                'class':'form-control p-2',
                'autocomplete':"off" 
            }),
            "phone": forms.TextInput(attrs={
                'class':'form-control p-2',
                'autocomplete':"off" 
            }),
            "email": forms.EmailInput(attrs={
                'class':'form-control p-2',
                'autocomplete':"off",
            }),
            "description": forms.TextInput(attrs={
                'class':'form-control p-2',
                'autocomplete':"off" 
            }),
        }

class ParticipantForm(forms.ModelForm):
    
    class Meta:
        model = Participant
        fields = ("organization","name","phone","email","role","project")
        
        labels = {
            "name": ("Nombre completo"),
            "phone": ("Teléfono de contacto"),
            "email": ("Correo Electronico"),
            "project": ("Proyecto al que pertenece"),
            "organization": ("Institución al que pertenece"),
        }
        
        widgets = {
            "project": forms.Select(attrs={
                'class':"form-select",
            }),
            "name": forms.TextInput(attrs={
                'class':'form-control',
                'autocomplete':"off",
            }),
            "phone": forms.TextInput(attrs={
                'class':'form-control p-2',
                'autocomplete':"off" 
            }),
            "email": forms.EmailInput(attrs={
                'class':'form-control p-2',
                'autocomplete':"off",
            }),
            "role": forms.RadioSelect(attrs={
                'class': ''
            }),
            "organization": forms.Select(attrs={
                'class':'form-select'
            }),
        }