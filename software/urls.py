from django.urls import path

from software.views import ObjectiveCreateView, ObjectiveListView
from software.views import RequerimentCreateView, RequerimentListView
from software.views import AppDescriptionUpdateView,AppDescriptionDetailView

urlpatterns = [
    path('<int:pk>/objective/new/', ObjectiveCreateView.as_view(), name="new_objective"),
    path('p/<int:pk>/', ObjectiveListView.as_view(), name="objectives"),
    path('<int:pk>/requeriment/new/', RequerimentCreateView.as_view(), name="new_requeriment"),
    path('p/<int:pk>/', RequerimentListView.as_view(), name="requeriments"),
    path('description/<int:pk>/edit/', AppDescriptionUpdateView.as_view(), name="edit_description"),
    path('description/<int:pk>/', AppDescriptionDetailView.as_view(), name="detail_description"),
]
