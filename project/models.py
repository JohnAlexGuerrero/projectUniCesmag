from django.db import models

from django.contrib.auth.models import User

from django.core import serializers

from django.shortcuts import get_object_or_404
from django.urls import reverse

from django_ckeditor_5.fields import CKEditor5Field

from post.models import Post, ProjectPost
from bot.models import Bot, Prompt
from component.models import Component

# Create your models here.

class Project(models.Model):
    name = models.TextField(max_length=20, null=False)
    title = models.CharField(max_length=150, unique=True, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Project")
        verbose_name_plural = ("Projects")
        ordering = ("-id",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
    

class Software(models.TextChoices):
    SOFTWARE_DE_APLICACION = "Software de Aplicación"
    SOFTWARE_DE_GESTION = "Software de Gestión"
    SOFTWARE_DE_PROGRAMACION = "Software de Programación"
    SOFTWARE_DE_SISTEMA = "Software de Sistema"

class Category(models.TextChoices):
    PRODUCTIVIDAD = "Productividad"
    CREATIVIDAD =  "Creatividad"
    COMUNICACION = "Comunicación"
    NEGOCIOS = "Negocios"
    PROGRAMACION = "Programación"
    ENTRETENIMIENTO = "Entretenimiento"
    EDUCACION = "Educativo"
    BIENESTAR_Y_SALUD = "Bienestar y Salud"

class Sector(models.TextChoices):
    ESTILO_DE_VIDA = "Estilo de Vida"
    SALUD = "Salud"
    EDUCACION = "Educación"
    FINANZAS_Y_ECONOMIA = "Finanzas y economia"
    MANUFACTURA = "Manufactura"
    TRANSPORTE_Y_LOGISTICA = "Transporte y logistica"
    AGRICULTURA = "Agricultura"
    GOBIERNO = "Gobierno"
    TELECOMUNICACIONES = "Telecomunicaciones"
    ENERGIA = "Energía"
    RECURSOS_HUMANOS = "Recursos Humanos"
    MARKETING = "Marketing"
    LEGAL = "Legal"
    CONSTRUCCION = "Construcción"
    TURISMO = "Turismo"
    BIENES_RAICES =	"Bienes Raíces"
    ENTRETENIMIENTO = "Entretenimiento"
    DEPORTES = "Deportes"
    CIENCIA_E_INVESTIGACION = "Ciencia e investigación"
    SERVICIOS_PUBLICOS = "Servicios Publicos"
    SOFTWARE = "Desarrollo de Software"
    CUIDADO_ANIMAL = "Cuidado Animal"
    
class License(models.TextChoices):
    PROPIETARIO = "Propietario"
    LIBRE = "Libre"
    CODIGO_ABIERTO = "Codigo Abierto"
    
class Categorization(models.Model):
    project = models.ForeignKey("project.Project", on_delete=models.CASCADE)
    license = models.CharField(("¿Cuál es el Tipo de licencia?"), max_length=50, choices=License.choices, default=License.PROPIETARIO)
    software = models.CharField(("¿Cuál es el Tipo de software, según sus funciones principales?"), max_length=150, choices=Software.choices, default=Software.SOFTWARE_DE_APLICACION)
    category = models.TextField(("Selecciona una categoría"), max_length=255, choices=Category.choices, default=Category.PRODUCTIVIDAD )
    sector = models.CharField(("¿En qué sector se encuentra el desarrollo de software?"), max_length=200, choices=Sector.choices)

    class Meta:
        verbose_name = ("Categorization")
        verbose_name_plural = ("Categorizations")

    def __str__(self):
        return self.project.title

    def get_absolute_url(self):
        return reverse("Categorization_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
 