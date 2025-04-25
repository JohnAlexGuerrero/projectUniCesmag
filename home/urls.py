from django.urls import path

from accounts.views import user_login
from home.views import HomeView, DashboardView, NewView

urlpatterns = [
    path('', user_login, name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('dashboard/menu/', NewView.as_view(), name='new_button'),
]
