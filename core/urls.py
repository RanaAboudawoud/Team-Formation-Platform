from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("projects/", views.projects, name = "projects"),
    path("register/", views.register, name = "register" ),
    path("login/", views.login_view, name = "login"),
    path("logout/", views.logout_view, name = "logout"),
    path("collaborator_profile/", views.collaborator_profile, name = "collaborator_profile"),
    path("idea_maker_profile/", views.idea_maker_profile, name = "idea_maker_profile"),
    path("create_project/", views.create_project, name = "create_project"),
]
