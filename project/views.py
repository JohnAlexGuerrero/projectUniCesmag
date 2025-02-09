from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import TemplateView

from project.models import Project, Categorization
from project.forms import ProjectForm, CategorizationForm

from post.models import Post, Module, ProjectPost

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
    
    def get_context_data(self, **kwargs) -> dict[str, object]:
        context = super().get_context_data(**kwargs)
        context['modules'] = [x[1] for x in Module.choices]
        context["posts"] = ProjectPost.objects.filter(project__id=self.object.id)
        return context
    

class ProjectUpdateView(UpdateView):
    model = Project
    template_name = "project/edit.html"
    form_class = ProjectForm
    
    def get_success_url(self):
        return redirect('detail', kwargs={'pk': self.object.id})
    
    def get_context_data(self, **kwargs) -> dict[str, object]:
        context = super().get_context_data(**kwargs)
        context["modules"] = [x[0] for x in Module.choices]
        context['posts'] = self.object.posts.all()
        return context
    

class ProductPostDetailView(DetailView):
    model = ProjectPost
    template_name = "post/detail.html"
    
    def get_context_data(self, **kwargs) -> dict[str, object]:
        context = super().get_context_data(**kwargs)
        context['modules'] = [x[1] for x in Module.choices]
        context["posts"] = ProjectPost.objects.filter(project__id=self.object.project.id)
        return context

class CategorizationView(CreateView):
    model = Categorization
    template_name = "project/categorization.html"
    form_class = CategorizationForm
    
    def get_success_url(self):
        return redirect('detail', kwargs={'pk': self.kwargs['pk']})
    
    def get_context_data(self, **kwargs) -> dict[str, object]:
        context = super().get_context_data(**kwargs)
        context['modules'] = [x[1] for x in Module.choices]
        context["posts"] = ProjectPost.objects.filter(project__id=self.kwargs['pk'])
        context['object'] = Project.objects.get(pk=self.kwargs['pk'])
        return context


def delete_project(request):
    p = Project.objects.get(pk=request.POST.get('pk'))
    p.delete()
    return redirect('list')