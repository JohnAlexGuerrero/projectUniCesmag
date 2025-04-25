from django.urls import reverse
from django.db import models

from io import BytesIO
from django.core.files import File
from PIL import Image

# Create your models here.
class Image(models.Model):
    title = models.CharField(("titulo"), max_length=50, unique=True)
    image = models.ImageField(("imagen"), upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    project = models.ForeignKey("project.Project",on_delete=models.CASCADE, related_name="images")
    is_logo = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = ("Image")
        verbose_name_plural = ("Images")
        ordering = ("-id",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Images_detail", kwargs={"pk": self.pk})
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
            
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
