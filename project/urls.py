from django.urls import path

from project.views import (
    ProjectCreateView,
    ProjectListView,
    ProjectDetailView,
    ProjectUpdateView,
    ProductPostDetailView,
    CategorizationView,
    ProjectDeleteView
)

from upload.views import (
    ImageCreateView,
    ImageListView,
    delete_image,
    ImageDetailView
)

from post.views import (
    PostCreateView,
    PostUpdateView, delete_post, writing_ai
)

from feature.views import (
    FeatureCreateView,
    FeatureDetailView,
    FeatureUpdateView,
    delete_feature
)

from author.views import (
    OrganizationDetailView, 
    OrganizationCreateView,
    OrganizationListView,
    OrganizationUpdateView,
    delete_organization,
    ParticipantCreateView,
    ParticipantListView
)

from software.views import ObjectiveCreateView


urlpatterns = [
    path('new/', ProjectCreateView.as_view(), name="new"),
    path('list/', ProjectListView.as_view(), name='list'),
    path('<int:pk>/detail/', ProjectDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', ProjectUpdateView.as_view(), name='update'),
    path('<int:pk>/categorization/', CategorizationView.as_view(), name='categorization'),
    path('<int:pk>/delete/', ProjectDeleteView.as_view(), name='delete_project'),
    
    path('<int:pk>/image/new/', ImageCreateView.as_view(), name='new_image'),
    path('<int:pk>/images/', ImageListView.as_view(), name='list_image'),
    path('image/<int:pk>/', ImageDetailView.as_view(), name='detail_image'),
    path('image/delete/', delete_image, name='delete_image'),
    
    path('<int:pk>/post/', PostCreateView.as_view(), name="new_post"),
    path('post/<int:pk>/detail/', ProductPostDetailView.as_view(), name='detail_post'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='edit_post'),
    path('post/delete/', delete_post, name='delete_post'),
    
    path('<int:pk>/feature/', FeatureCreateView.as_view(), name='new_feature'),
    path('feat/<int:pk>/detail/', FeatureDetailView.as_view(), name='detail_feature'),
    path('feat/<int:pk>/edit/', FeatureUpdateView.as_view(), name='edit_feature'),
    path('feat/delete/', delete_feature, name='delete_feature'),
    
    path('bot/write/', writing_ai, name='bot_write'),
    
    path('teams/', OrganizationCreateView.as_view(), name="new_organization"),
    path('<int:pk>/teams/organizations/', OrganizationListView.as_view(), name="organizations"),
    path('teams/organization/<int:pk>/', OrganizationUpdateView.as_view(), name="edit_organization"),
    path('teams/organization/<int:pk>/detail/', OrganizationDetailView.as_view(), name="detail_organization"),
    path('teams/organization/delete/', delete_organization, name="delete_organization"),
    
    path('teams/participant/', ParticipantCreateView.as_view(), name="new_participant"),
    path('<int:pk>/teams/participant/', ParticipantListView.as_view(), name="participants"),
    

    # path("upload/", custom_upload_function, name="custom_upload_file"),
]
