from django.urls import path

from project.views import (
    ProjectCreateView,
    ProjectListView,
    ProjectDetailView,
    ProjectUpdateView,
    delete_project
)

from upload.views import (
    ImageCreateView,
    delete_image
)

urlpatterns = [
    path('new/', ProjectCreateView.as_view(), name="new"),
    path('list/', ProjectListView.as_view(), name='list'),
    path('<int:pk>/detail/', ProjectDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', ProjectUpdateView.as_view(), name='update'),
    path('delete/', delete_project, name='delete'),
    
    path('<int:pk>/image/new/', ImageCreateView.as_view(), name='new_image'),
    path('image/delete/', delete_image, name='delete_image'),
]
