from django.db import models

from django.shortcuts import get_object_or_404
from django.urls import reverse

from django_ckeditor_5.fields import CKEditor5Field

from post.models import Post, ProjectPost

# Create your models here.

class Project(models.Model):
    title = models.CharField(("titulo"), max_length=150, unique=True, null=False)
    description = CKEditor5Field('descrición', config_name='extends')
    version = models.CharField(("version"), max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = ("Project")
        verbose_name_plural = ("Projects")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        for post in Post.objects.all():
            obj, obj_created = ProjectPost.objects.get_or_create(
                    title=post.title, 
                    defaults={'project':self, 'title':post.title, 'content': post.content, 'module': post.module}
                )
            
            if obj_created:
                print(obj_created)
            else:
                print(f"{obj} it´s exist...")
            
        return f"saved..."
    
'''

'''
class Software(models.TextChoices):
    ANTHIVIRUS = 'Anthivirus'
    BUSINESS_INTELLIGENCE_BI = 'Business Intelligence BI'
    CUIDADO_DE_MASCOTAS = 'Cuidado De Mascotas'
    CALCULO_Y_ANALISIS_DE_DATOS = 'Calculo Y Analisis De Datos'
    CORREO_ELECTRONICO = 'Correo Electronico'
    CREACION_DE_CONTENIDO_MULTIMEDIA = 'Creacion De Contenido Multimedia'
    CREACION_DE_DOCUMENTOS = 'Creacion De Documentos'
    CALENDARIOS = 'Calendarios'
    COMPRESOR_DE_ARCHIVOS = 'Compresor De Archivos'
    CURSOS_EN_LINEA = 'Cursos En Linea'
    CONTABILIDAD_Y_FINANZAS = 'Contabilidad Y Finanzas'
    DESARROLLO_DE_SOFTWARE = 'Desarrollo De Software'
    DISEÑO_GRAFICO = 'Diseño Grafico'
    DISEÑO_Y_MODELADO = 'Diseño Y Modelado'
    EDUCACION_Y_APRENDIZAJE = 'Educacion Y Aprendizaje'
    EDITORES_DE_IMAGENES = 'Editores De Imagenes'
    E_COMMERCE = "E commerce"
    EDITORES_DE_VIDEO = 'Editores De Video'
    GESTION_BASES_DATOS = 'Gestion Bases De Datos'
    GESTION_DE_ARCHIVOS_Y_CARPETAS = 'Gestion De Archivos y carpetas'
    GESTION_DE_DISPOSITIVOS = 'Gestion De Dispositivos'
    GESTION_DE_TAREAS = 'Gestion De Tareas'
    HOJAS_DE_CALCULO = 'Hojas De Calculo'
    GESTION_DE_RELACIONES_CON_CLIENTES_CRM = 'Gestion De Relaciones Con Clientes CRM'
    GESTION_DEL_TIEMPO = 'Gestion Del Tiempo'
    GESTION_DE_PROYECTOS = 'Gestion De Proyectos'
    HERRAMIENTAS_EDUCATIVAS = 'Herramientas Educativas'
    HERRAMIENTAS_DE_MINERIA_DE_DATOS = "Herramientas De Mineria De Datos"
    HERRAMIENTAS_DE_INTELIGENCIA_ARTIFICIAL = "Herramientas De Inteligencia Artificial"
    JUEGOS = 'Juegos'
    LIBROS_ELECTRONICOS = 'Libros Electronicos'
    MESANGERIA_INSTANTANEA = 'Mensajeria Instantanea'
    NOTAS = 'Notas'
    NAVEGADORES_WEB = 'Navegadores Web'
    PRESENTACIONES = 'Presentaciones'
    PROCESAMIENTO_DE_TEXTOS = 'Procesamiento De Textos'
    REDES_SOCIALES = 'Redes Sociales'
    REPRODUCCION_MULTIMEDIA_DE_AUDIO_Y_VIDEO = 'Reproducción Multimedia De Audio Y Video'
    SOFTWARE_DE_MUSICA = 'Software_De_Musica'
    SERVICIOS_DE_TRANSMISION = 'Servicios De Transmision'
    SOFTWARE_DE_IDIOMAS = 'Software De Idiomas'
    SALUD_Y_CUIDADO_PERSONAL = 'Salud Y Cuidado Personal'
    SEGURIDAD_INFORMATICA = 'Seguridad Informatica'
    TRADUCCION_DE_IDIOMAS = 'Traduccion De Idiomas'
    VIDEOLLAMADAS = 'Videollamadas'

class Category(models.TextChoices):
    PRODUCTIVIDAD = "Software de productividad ayuda a los usuarios a realizar tareas comunes de manera más eficiente."
    CREATIVIDAD =  "Software de creatividad ayuda a los usuarios a crear contenido multimedia, como imágenes, videos y música."
    COMUNICACION = "El software de comunicación ayuda a los usuarios a comunicarse con otros."
    NEGOCIOS = "El software empresarial ayuda a las empresas a realizar sus operaciones."
    PROGRAMACION = "El software de programación ayuda a los desarrolladores a crear distintas aplicaciones."
    ENTRETENIMIENTO = "El software de entretenimiento ayuda a los usuarios a relajarse y divertirse."
    EDUCACION = "El software educativo ayuda a los usuarios a aprender cosas nuevas."
    BIENESTAR_Y_SALUD = "El software de bienestar se enfoca en el cuidado de la salud de los usuarios."

class Sector(models.TextChoices):
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
    
class License(models.TextChoices):
    PROPIETARIO = "Propietario"
    LIBRE = "Libre"
    CODIGO_ABIERTO = "Codigo Abierto"
    
class Categorization(models.Model):
    project = models.ForeignKey("project.Project", on_delete=models.CASCADE)
    license = models.CharField(("Tipo de licencia"), max_length=50, choices=License.choices, default=License.PROPIETARIO)
    software = models.CharField(("Tipo de software"), max_length=150, choices=Software.choices)
    category = models.TextField(("Categoría"), max_length=255, choices=Category.choices, default=Category.PRODUCTIVIDAD )
    sector = models.CharField(("sector"), max_length=200, choices=Sector.choices)

    class Meta:
        verbose_name = ("Categorization")
        verbose_name_plural = ("Categorizations")

    def __str__(self):
        return self.project.title

    def get_absolute_url(self):
        return reverse("Categorization_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        obj, created = ProjectPost.objects.get_or_create(
            title="Categorización de software",
            defaults={"project":self.project, 
                      "title":"Categorización de software", 
                      "content": f"{self.license} - {self.sector} - {self.software} - {self.category}", 
                      "module": "Introducción"
            }
        )
        
        if created:
            print("created with exit.")
        else:
            print("it exist.")
            
        return super().save(*args, **kwargs)