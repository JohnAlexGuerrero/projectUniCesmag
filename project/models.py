from django.db import models
from django.urls import reverse

# Create your models here.

class Project(models.Model):
    title = models.CharField(("titulo"), max_length=150, unique=True, null=False)
    description = models.TextField(("description"))

    class Meta:
        verbose_name = ("Project")
        verbose_name_plural = ("Projects")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})

