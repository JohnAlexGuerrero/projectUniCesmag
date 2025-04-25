from django.db.models.signals import post_save
from django.dispatch import receiver

from project.models import Project
from software.models import App

@receiver(post_save, sender=Project)
def create_software(sender, instance, created, **kwargs):
    if created:
        App.objects.create(
            name=instance.name,
            project=instance
        )