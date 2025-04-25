from django.shortcuts import render

from post.models import Post

from django.contrib.auth.models import User
from project.models import Project

from django.views.generic import ListView
from django.views.generic import TemplateView

from accounts.forms import LoginForm
from project.forms import ProjectForm


class HomeView(TemplateView):
    template_name = "accounts/login.html"
    
    def get_context_data(self, **kwargs) -> dict[str, object]:
        context = super().get_context_data(**kwargs)
        context["form"] = LoginForm
        return context
    
    
    
    
class DashboardView(TemplateView):
    template_name = "home/dashboard.html"

    def get_context_data(self, **kwargs) -> dict[str, object]:
        context = super().get_context_data(**kwargs)
        context["objects"] = Project.objects.filter(user=self.request.user)
        context['form'] = ProjectForm
        return context
    
    


class PostListView(ListView):
    model = Post
    template_name = "includes/sidebar.html"

class NewView(TemplateView):
    template_name = "includes/menu.html"
