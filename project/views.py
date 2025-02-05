from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView

from project.models import Project
from project.forms import ProjectForm

# Create your views here.
class ProjectCreateView(CreateView):
    model = Project
    template_name = "project/new.html"
    form_class = ProjectForm
    
    def get_queryset(self):
        return self.id
    
    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.id})
    

class ProjectListView(ListView):
    model = Project
    template_name = "project/list.html"

class ProjectDetailView(DetailView):
    model = Project
    template_name = "project/detail.html"

class ProjectUpdateView(UpdateView):
    model = Project
    template_name = "project/edit.html"
    form_class = ProjectForm
    success_url = reverse_lazy('list')

def delete_project(request):
    p = Project.objects.get(pk=request.POST.get('pk'))
    p.delete()
    return redirect('list')