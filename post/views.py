from django.shortcuts import render, redirect

from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView

from post.models import Post, Module, ProjectPost
from post.forms import PostForm

# Create your views here.

class PostCreateView(CreateView):
    model = ProjectPost
    template_name = "post/new.html"
    form_class = PostForm
    
    def get_success_url(self):
        return redirect("detail", kwargs={'pk': self.object.project.id})

class PostUpdateView(UpdateView):
    model = ProjectPost
    template_name = "post/edit.html"
    form_class = PostForm
    
    def get_success_url(self):
        return redirect("detail_post", kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs) -> dict[str, object]:
        context = super().get_context_data(**kwargs)
        context['modules'] = [x[0] for x in Module.choices]
        context["posts"] = self.object.project.posts.all()
        # print(self.object.project.posts.all())
        print(context)
        return context
    