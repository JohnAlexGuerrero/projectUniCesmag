from django.urls import path

from project.views import (
    ProjectCreateView,
    ProjectListView,
    ProjectDetailView,
    ProjectUpdateView
)

urlpatterns = [
    path('new/', ProjectCreateView.as_view(), name="new"),
    path('list/', ProjectListView.as_view(), name='list'),
    path('<int:pk>/detail/', ProjectDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', ProjectUpdateView.as_view(), name='update'),
]
