from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    )

    phone_number = models.CharField(max_length = 20)

    ROLE_CHOICES = [
        ("collaborator","Collaborator"),
        ("idea_maker", "Idea Maker"),
    ]

    role = models.CharField(max_length = 20, choices = ROLE_CHOICES)

class Collaborator_profile(models.Model):
    profile = models.OneToOneField(Profile, on_delete = models.CASCADE)
    availability = models.IntegerField()

class Project(models.Model):
    name = models.CharField(max_length = 200)
    req_hours = models.IntegerField()

class Skill(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Project_skill(models.Model):
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete = models.CASCADE)

    PROFICIENCY_CHOICES = [
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
        ("expert", "Expert"),
    ]

    required_proficiency = models.CharField(max_length = 200, choices = PROFICIENCY_CHOICES)

class Collaborator_skill(models.Model):
    collaborator = models.ForeignKey(Collaborator_profile, on_delete = models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete = models.CASCADE)

    proficiency = models.CharField(max_length = 200, choices = Project_skill.PROFICIENCY_CHOICES)