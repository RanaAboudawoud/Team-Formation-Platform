from .models import Project_interest
from .matching import calculate_project_score

def get_interested_collaborators(project):
    interests = Project_interest.objects.filter(project = project)

    collaborators = []

    for interest in interests:
        collaborators.append(interest.collaborator)

    return collaborators

def calculate_collaborator_match_score(collaborator, project, skill_weight = 0.25, availability_weight = 0.25, sector_weight = 0.25, commitment_weight = 0.25):
    return calculate_project_score(collaborator, project, skill_weight = skill_weight, availability_weight = availability_weight, sector_weight = sector_weight, commitment_weight = commitment_weight)