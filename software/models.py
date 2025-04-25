from django.db import models

from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class App(models.Model):
    class Category(models.TextChoices):
        APLICACION_WEB = 'Aplicacion Web'
        APLICACION_ESCRITORIO = 'Aplicacion Escritorio'
        APLICACION_MOVIL = 'Aplicacion Movil'
        APLICACION_IOT = 'Aplicacion IoT'
        MENSAJERIA = 'Mensajeria'
        INTELIGENCIA_ARTIFICIAL = 'Inteligencia Artificial'
        
        
    name = models.CharField(max_length=20, unique=True, null=False)
    description = CKEditor5Field("", config_name="extends")
    verse = models.CharField(max_length=10, null=True, blank=True)
    category = models.CharField(max_length=50, choices=Category.choices, default=Category.APLICACION_WEB)
    project = models.OneToOneField("project.Project", on_delete=models.CASCADE, related_name='software')
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = ("App")
        verbose_name_plural = ("Apps")

    def __str__(self):
        return self.name

class Hardware(models.Model):
    class TypeHardware(models.TextChoices):
        ALMACENAMIENTO = "Almacenamiento"
        MEMORIA_RAM = "Memoria Ram"
        PROCESADOR = "Procesador"
        PANTALLA = "Pantalla"
        OTRO_DISPOSITIVO = "Otro dispositivo"
        
    title = models.CharField(max_length=50)
    project = models.ForeignKey("software.App", on_delete=models.CASCADE, related_name="hardware")
    type = models.CharField(max_length=50, choices=TypeHardware.choices)

    class Meta:
        verbose_name = ("Hardware")
        verbose_name_plural = ("Hardwares")

    def __str__(self):
        return self.title

class ExternalSoftware(models.Model):
    class TypeSoftware(models.TextChoices):
        SERVIDOR_DE_APLICACIONES = "Servidor de aplicaciones"
        SISTEMA_GESTOR_DE_BASE_DE_DATOS = "Sistema gestor de base de datos"
        SISTEMA_OPERATIVO_DE_DESPLIEGUE = "Sistema operativo de despliegue"
        NAVEGADOR_WEB = "Navegador web"
        MOTOR_DE_BASE_DE_DATOS = "Motor de bases de datos"
        
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=TypeSoftware.choices)
    project = models.ForeignKey("software.ExternalSoftware", on_delete=models.CASCADE, related_name="externals")

    class Meta:
        verbose_name = ("Software")
        verbose_name_plural = ("Softwares")

    def __str__(self):
        return self.name
    

class BaseModel(models.Model):
    title = models.CharField(max_length=150)
    version = models.CharField(max_length=20)
    fuente = models.CharField(max_length=50)
    description = models.TextField()
    importancia = models.CharField(max_length=50, choices=[('Esencial','Esencial'),('Prescindible','Prescindible')], default=[('Esencial','Esencial'),('Prescindible','Prescindible')][0])
    urgencia = models.CharField(max_length=50, choices=[('Inmediata','Inmediata'),('Puede esperar','Puede esperar')],default=[('Inmediata','Inmediata'),('Puede esperar','Puede esperar')][0])
    status = models.CharField( max_length=50, choices=[('Implementado','Implementado'),('Pendiente','Pendiente')], default=[('Implementado','Implementado'),('Pendiente','Pendiente')][0])
    estabilidad = models.CharField(max_length=50, choices=[('Baja','Baja'),('Media','Media'),('Alta','Alta')],default=[('Baja','Baja'),('Media','Media'),('Alta','Alta')][0])
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    

    class Meta:
        abstract = True
    


class Objective(BaseModel):
    objectiveId = models.CharField(max_length=10, null=True, blank=True)
    software = models.ForeignKey("software.App", on_delete=models.CASCADE, related_name="objectives")
    authors = models.ManyToManyField("author.Participant", related_name="authors")


    class Meta:
        verbose_name = ("Objective")
        verbose_name_plural = ("Objectives")

    def __str__(self):
        return self.title

class Requeriment(BaseModel):
    software = models.ForeignKey("software.App", on_delete=models.CASCADE, related_name="requeriments")
    authors = models.ManyToManyField("author.Participant", related_name="author")

    class Meta:
        verbose_name = ("Requeriment")
        verbose_name_plural = ("Requeriments")

    def __str__(self):
        return self.title

