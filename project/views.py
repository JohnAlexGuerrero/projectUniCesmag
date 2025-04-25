from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from project.models import Project, Categorization
from author.models import Organization

from project.forms import ProjectForm, CategorizationForm
from author.forms import OrganizationForm, ParticipantForm
from upload.forms import ImageForm

from post.models import Post, Module, ProjectPost

# Create your views here.
class ProjectCreateView(LoginRequiredMixin,CreateView):
    model = Project
    template_name = "project/new.html"
    form_class = ProjectForm
    
    def get_success_url(self):
        return reverse_lazy('dashboard')
    

class ProjectListView(ListView):
    model = Project
    template_name = "project/list.html"
    
    def get_context_data(self, **kwargs) -> dict[str, object]:
        context = super().get_context_data(**kwargs)
        context["form"] = ProjectForm
        return context
    

class ProjectDetailView(LoginRequiredMixin,DetailView):
    model = Project
    template_name = "project/detail.html"
    
    def get_context_data(self, **kwargs) -> dict[str, object]:
        context = super().get_context_data(**kwargs)
        context["ParticipantForm"] = ParticipantForm()
        context["OrganizationForm"] = OrganizationForm()
        context["ImageForm"] = ImageForm
        print(context)
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
        return reverse_lazy('detail', kwargs={'pk': self.object.project.id})
    
    def get_context_data(self, **kwargs) -> dict[str, object]:
        context = super().get_context_data(**kwargs)
        context['modules'] = [x[1] for x in Module.choices]
        context["posts"] = ProjectPost.objects.filter(project__id=self.kwargs['pk'])
        context['object'] = Project.objects.get(pk=self.kwargs['pk'])
        return context


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = "project/delete.html"
    success_url = reverse_lazy('dashboard')
