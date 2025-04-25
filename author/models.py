from django.db import models

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    description = models.TextField( null=True, blank=True)
    project = models.ForeignKey("project.Project", on_delete=models.CASCADE, related_name="organizations")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = ("Organization")
        verbose_name_plural = ("Organizations")

    def __str__(self):
        return self.name


class Participant(models.Model):
    class Type(models.TextChoices):
        DIRECTOR_DE_PROYECTO = "Director de proyecto"
        DESARROLLADOR = "Desarrollador"
        INVESTIGADOR = "Investigador"
        DESARROLLADOR_E_INVESTIGADOR = "Desarrollador e Investigador"
        CLIENTE = "Cliente"
        USUARIO = "Usuario"
        
    name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    role = models.CharField(max_length=150, choices=Type.choices, default=Type.DESARROLLADOR)
    organization = models.ForeignKey("author.Organization", on_delete=models.CASCADE, related_name="organization")
    project = models.ForeignKey("project.Project", on_delete=models.CASCADE, related_name="participants")
    
    class Meta:
        verbose_name = ("Participant")
        verbose_name_plural = ("Participants")

    def __str__(self):
        return self.name

