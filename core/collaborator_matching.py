from .models import Project_interest
from .matching import calculate_project_score, get_match_level, get_recommended_reasons, get_non_matching_reasons
from operator import itemgetter

def get_interested_collaborators(project):
    interests = Project_interest.objects.filter(project = project)

    collaborators = []

    for interest in interests:
        collaborators.append(interest.collaborator)

    return collaborators

def calculate_collaborator_match_score(collaborator, project, skill_weight = 0.25, availability_weight = 0.25, sector_weight = 0.25, commitment_weight = 0.25):
    return calculate_project_score(collaborator, project, skill_weight = skill_weight, availability_weight = availability_weight, sector_weight = sector_weight, commitment_weight = commitment_weight)

def filter_collaborators_by_availability(collaborators, project):
    available_collaborators = []

    for collaborator in collaborators:
        if collaborator.availability >= project.req_hours:
            available_collaborators.append(collaborator)

    return available_collaborators

def rank_interested_collaborators(project):
    interested_collaborators = get_interested_collaborators(project)

    available_collaborators = filter_collaborators_by_availability(interested_collaborators, project)

    ranked_collaborators = []

    for collaborator in available_collaborators:
        score = calculate_collaborator_match_score(collaborator, project)
        match_level = get_match_level(score)
        reasons = get_recommended_reasons(collaborator, project)
        non_matching_reasons = get_non_matching_reasons(collaborator, project)

        ranked_collaborators.append((collaborator, score, match_level, reasons, non_matching_reasons))

    ranked_collaborators.sort(key = itemgetter(1), reverse = True)

    return ranked_collaborators