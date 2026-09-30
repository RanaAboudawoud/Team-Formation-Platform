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

class Idea_maker_profile(models.Model):
    profile = models.OneToOneField(Profile, on_delete = models.CASCADE)
    bio = models.TextField(max_length = 1000, blank = True)

class Project(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField(max_length = 1000)

    CATEGORY_CHOICES = [
        ("technology", "Technology"),
        ("marketing", "Marketing"),
        ("writing", "Writing & Content"),
        ("design", "Design"),
        ("business", "Business"),
        ("education", "Education"),
        ("health", "Health & Wellness"),
        ("environment", "Environment & Sustainability"),
        ("media", "Media & Entertainment"),
        ("other", "Other"),
    ]

    STAGE_CHOICES = [
        ("idea", "Idea"),
        ("planning", "Planning"),
        ("in_development", "In Development"),
        ("launched", "Launched"),
    ]

    COMPENSATION_CHOICES = [
        ("salary", "Salary"),
        ("equity", "Equity (Ownership)"),
        ("revenue_sharing", "Revenue Sharing"),
        ("volunteer", "Volunteer / Unpaid"),
        ("negotiable", "To Be Discussed"),
    ]

    REQ_HOURS_CHOICES = [
        (5, "1-5 hours/week"),
        (10, "5-10 hours/week"),
        (15, "10-15 hours/week"),
        (20, "15-20 hours/week"),
        (25, "20+ hours/week"),
    ]

    req_hours = models.IntegerField(choices = REQ_HOURS_CHOICES)
    category = models.CharField(max_length = 100, choices = CATEGORY_CHOICES)
    stage = models.CharField(max_length = 100, choices = STAGE_CHOICES)
    compensation = models.CharField(max_length = 100, choices = COMPENSATION_CHOICES)

    idea_maker = models.ForeignKey(Idea_maker_profile, on_delete = models.CASCADE)

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