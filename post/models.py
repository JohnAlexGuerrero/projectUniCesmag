from django.urls import reverse

from django.db import models

from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Module(models.TextChoices):
    INTRODUCCIóN = 'Introducción'
    INSTALACIóN = 'Instalación'
    INICIO_RÁPIDO = 'Inicio Rápido'
    FUNCIONALIDADES_PRINCIPALES = 'Funcionalidades Principales'
    CONFIGURACIÓN_AVANZADA = 'Configuración Avanzada'
    SOLUCIÓN_DE_PROBLEMAS = 'Solución de Problemas'
    SOPORTE_Y_CONTACTO = 'Soporte y Contacto'
    APENDICE = 'Apendice'

class Post(models.Model):
    title = models.CharField(("titulo"), max_length=150)
    content = CKEditor5Field("contenido", config_name="extends")
    module = models.CharField(("modulo"), max_length=50, choices=Module.choices)

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail_post", kwargs={"pk": self.pk})

    
class ProjectPost(models.Model):
    project = models.ForeignKey("project.Project", on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(("titulo"), max_length=50)
    content = CKEditor5Field(("Contenido"), config_name="extends")
    module = models.CharField(("modulo"), max_length=50)
    

    class Meta:
        verbose_name = ("ProjectPost")
        verbose_name_plural = ("ProjectPosts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail_post", kwargs={"pk": self.pk})
