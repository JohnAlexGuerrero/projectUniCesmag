from django.shortcuts import render
from django.urls import reverse_lazy

from software.models import App, Objective, Requeriment
from project.models import Project

from software.forms import ObjectiveForm, RequerimentForm, AppDescriptionForm

from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DetailView
# Create your views here.

class ObjectiveCreateView(CreateView):
    model = Objective
    template_name = "software/objective/new.html"
    form_class = ObjectiveForm
    
    def get_success_url(self):
        return reverse_lazy('objectives', kwargs={'pk':self.kwargs['pk']})
    
    def get_context_data(self, **kwargs) -> dict[str, object]:
        context = super().get_context_data(**kwargs)
        project = Project.objects.get(pk=self.kwargs['pk'])
        software = project.software
        context["form"] = ObjectiveForm(project__id=project.id, software__id=software.id)
        context['object'] = project
        context["software"] = software
        return context
    
    
class ObjectiveListView(ListView):
    model = Objective
    template_name = "software/objective/list.html"
    
    def get_context_data(self, **kwargs) -> dict[str, object]:
        context = super().get_context_data(**kwargs)
        project = Project.objects.get(pk=self.kwargs['pk'])
        context["object_list"] = project.software.objectives.all()
        context["object"] = project
        return context
    
    
class RequerimentListView(ListView):
    model = Requeriment
    template_name = "software/Requeriment/list.html"
    
    def get_context_data(self, **kwargs) -> dict[str, object]:
        context = super().get_context_data(**kwargs)
        project = Project.objects.get(pk=self.kwargs['pk'])
        context["object_list"] = project.software.objectives.all()
        return context
    
class RequerimentCreateView(CreateView):
    model = Requeriment
    template_name = "software/requeriment/new.html"
    form_class = RequerimentForm
    
    def get_success_url(self):
        return reverse_lazy('requeriments', kwargs={'pk':self.kwargs['pk']})
    
    def get_context_data(self, **kwargs) -> dict[str, object]:
        context = super().get_context_data(**kwargs)
        project = Project.objects.get(pk=self.kwargs['pk'])
        software = project.software
        context["form"] = ObjectiveForm(project__id=project.id)
        context['object'] = project
        context["software"] = software
        return context

class AppDescriptionUpdateView(UpdateView):
    model = App
    template_name = "software/description/new.html"
    form_class = AppDescriptionForm
    
    def get_success_url(self):
        return reverse_lazy('detail_description', kwargs={'pk':self.object.id})
    
    def get_context_data(self, **kwargs) -> dict[str, object]:
        context = super().get_context_data(**kwargs)
        context["object"] = self.object
        return context

class AppDescriptionDetailView(DetailView):
    model = App
    template_name = "software/description/detail.html"
