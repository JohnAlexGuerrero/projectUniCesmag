from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from author.models import Participant, Organization
from project.models import Project

from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from author.forms import OrganizationForm, ParticipantForm
# Create your views here.

class ParticipantDetailView(DetailView):
    model = Project
    template_name = "author/detail.html"

    def get_context_data(self, **kwargs) -> dict[str, object]:
        context = super().get_context_data(**kwargs)
        context["participants"] = self.object.participants.all()
        print(context)
        return context
    
class OrganizationCreateView(CreateView):
    model = Organization
    template_name = "author/organization/new.html"
    form_class = OrganizationForm
    
    def get_context_data(self, **kwargs) -> dict[str, object]:
        context = super().get_context_data(**kwargs)
        return context
    
    
    def get_success_url(self):
        return reverse_lazy('organizations', kwargs={'pk': self.object.project.id})
    
    
class OrganizationListView(ListView):
    model = Organization
    template_name = "author/organization/list.html"
    
    def get_context_data(self, **kwargs) -> dict[str, object]:
        context = super().get_context_data(**kwargs)
        context["object_list"] = Organization.objects.filter(project__id=self.kwargs['pk'])
        print(context)
        return context
    
    
    

class OrganizationUpdateView(UpdateView):
    model = Organization
    template_name = "author/form.html"
    form_class = OrganizationForm
    
    def get_success_url(self):
        return reverse_lazy("detail_organization", kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs) -> dict[str, object]:
        context = super().get_context_data(**kwargs)
        context["object"] = self.object
        return context
    

class OrganizationDetailView(DetailView):
    model = Organization
    template_name = "author/organization/detail.html"
     
 
def delete_organization(request):
    org = get_object_or_404(Organization, pk=request.POST.get('pk'))
    print(org)
    if request.method == 'POST':
        pk = org.project.id
        project = Project.objects.get(pk=org.project.id)
        org.delete()
        return reverse_lazy('organizations', kwargs={'pk':pk})
        
    return ''

class ParticipantCreateView(CreateView):
    model = Participant
    template_name = "author/new.html"
    form_class = ParticipantForm

    def get_success_url(self):
        return reverse_lazy('participants', kwargs={'pk': self.request.POST.get('project')})

class ParticipantListView(ListView):
    model = Participant
    template_name = "author/list.html"
    
    def get_context_data(self, **kwargs) -> dict[str, object]:
        context = super().get_context_data(**kwargs)
        context["object_list"] = Participant.objects.filter(project__id=self.kwargs['pk'])
        return context
    
