from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from upload.models import Image
from upload.forms import ImageForm

from project.models import Project

from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView

# Create your views here.
class ImageCreateView(CreateView):
    model = Image
    template_name = "upload/new.html"
    form_class = ImageForm
    
    def get_success_url(self):
        return reverse_lazy('list_image', kwargs={'pk': self.object.project.id})
    
    def get_context_data(self, **kwargs) -> dict[str, Project]:
        context = super().get_context_data(**kwargs)
        object = Project.objects.get(pk=self.kwargs['pk'])
        context["object"] = object
        return context
    
class ImageDetailView(DetailView):
    model = Image
    template_name = "upload/detail.html"
    
def delete_image(request):
    img = Image.objects.get(pk=request.POST.get('pk'))
    object = img.project
    img.delete()
    return reverse("detail", kwargs={'pk': object.id}) #render(request, 'project/detail.html', {'url': reverse("detail", kwargs={"pk": object.id })})


class ImageListView(ListView):
    model = Image
    template_name = "upload/list.html"
    
    def get_context_data(self, **kwargs) -> dict[str, object]:
        context = super().get_context_data(**kwargs)
        context["object_list"] = Image.objects.filter(project__id=self.kwargs['pk'])
        return context
    
