from django.urls import path

from project.views import (
    ProjectCreateView,
    ProjectListView,
    ProjectDetailView,
    ProjectUpdateView,
    ProductPostDetailView,
    CategorizationView,
    delete_project
)

from upload.views import (
    ImageCreateView,
    delete_image
)

from post.views import (
    PostCreateView,
    PostUpdateView,
)

urlpatterns = [
    path('new/', ProjectCreateView.as_view(), name="new"),
    path('list/', ProjectListView.as_view(), name='list'),
    path('<int:pk>/detail/', ProjectDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', ProjectUpdateView.as_view(), name='update'),
    path('<int:pk>/categorization/', CategorizationView.as_view(), name='categorization'),
    path('delete/', delete_project, name='delete'),
    
    path('<int:pk>/image/new/', ImageCreateView.as_view(), name='new_image'),
    path('image/delete/', delete_image, name='delete_image'),
    
    path('<int:pk>/post/', PostCreateView.as_view(), name="new_post"),
    path('post/<int:pk>/detail/', ProductPostDetailView.as_view(), name='detail_post'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='edit_post'),
    
]
