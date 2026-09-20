from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("projects/", views.projects, name = "projects"),
    path("register/", views.register, name = "register" ),
    path("collaborator_profile/", views.collaborator_profile, name = "collaborator_profile")
]
