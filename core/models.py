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

    AVAILABILITY_CHOICES = [
        (5, "1-5 hours/week"),
        (10, "5-10 hours/week"),
        (15, "10-15 hours/week"),
        (20, "15-20 hours/week"),
        (25, "20+ hours/week")
    ]

    COMMITMENT_CHOICES = [
        ("hobby", "Hobby"),
        ("side_project", "Side Project"),
        ("half_time", "Half Time"),
        ("full_time", "Full Time")
    ]

    availability = models.IntegerField(choices = AVAILABILITY_CHOICES)
    commitment = models.CharField(max_length = 20, choices = COMMITMENT_CHOICES)
    sector_interests = models.JSONField(default = list)

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

class Project_role(models.Model):
    ROLE_CHOICES = [
        ("software_developer", "Software Developer"),
        ("web_developer", "Web Developer"),
        ("data_analyst", "Data Analyst"),
        ("ui_ux_designer", "UI/UX Designer"),
        ("graphic_designer", "Graphic Designer"),
        ("marketing_specialist", "Marketing Specialist"),
        ("content_writer", "Content Writer"),
        ("business_developer", "Business Developer"),
        ("project_manager", "Project Manager"),
        ("educator_trainer", "Educator / Trainer"),
        ("health_specialist", "Health & Wellnes Specialist"),
        ("sustainability_specialist", "Sustainability Specialist"),
        ("media_producer", "Media Producer"),
        ("researcher", "Researcher"),
        ("consultant", "Consultant"),
        ("other", "Other"),
    ]

    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    role = models.CharField(max_length = 200, choices = ROLE_CHOICES)

    def __str__(self):
        return self.get_role_display()

class Skill(models.Model):
    SKILL_CHOICES = [
        ("python", "Python"),
        ("javascript", "JavaScript"),
        ("java", "Java"),
        ("html_css", "HTML & CSS"),
        ("django", "Django"),
        ("react", "React"),
        ("game_development", "Game Development"),
        ("sql", "SQL"),
        ("data_analysis", "Data Analysis"),
        ("machine_learning", "Machine Learning"),
        ("ui_ux_design", "UI/UX Design"),
        ("graphic_design", "Graphic Design"),
        ("figma", "Figma"),
        ("digital_marketing", "Digital Marketing"),
        ("social_media", "Social Media"),
        ("seo", "SEO"),
        ("content_writing", "Content Writing"),
        ("copywriting", "Copywriting"),
        ("business_strategy", "Business Strategy"),
        ("project_management", "Project Management"),
        ("sales", "Sales"),
        ("research", "Research"),
        ("teaching", "Teaching"),
        ("health_wellness", "Health & Wellness"),
        ("sustainability", "Sustainability"),
        ("video_production", "Video Production"),
        ("communication", "Communication"),
    ]

    name = models.CharField(max_length = 200, choices = SKILL_CHOICES, unique = True)

    def __str__(self):
        return self.get_name_display()

class Project_skill(models.Model):
    project_role = models.ForeignKey(Project_role, on_delete = models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete = models.CASCADE)

    PROFICIENCY_CHOICES = [
        ("learning", "Learning"),
        ("familiar", "Familiar"),
        ("competent", "Competent"),
        ("expert", "Expert"),
    ]

    required_proficiency = models.CharField(max_length = 200, choices = PROFICIENCY_CHOICES)

class Collaborator_skill(models.Model):
    collaborator = models.ForeignKey(Collaborator_profile, on_delete = models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete = models.CASCADE)

    proficiency = models.CharField(max_length = 200, choices = Project_skill.PROFICIENCY_CHOICES)

class Project_interest(models.Model):
    collaborator = models.ForeignKey(Collaborator_profile, on_delete = models.CASCADE)
    project = models.ForeignKey(Project, on_delete = models.CASCADE)