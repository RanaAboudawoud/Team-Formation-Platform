from .models import Collaborator_skill, Project_skill, Project
from operator import itemgetter

proficiency_levels = {
    "learning": 1, 
    "familiar": 2, 
    "competent": 3, 
    "expert": 4
    }

def proficiency_matching(collaborator_proficiency, required_proficiency):
    return proficiency_levels[collaborator_proficiency] >= proficiency_levels[required_proficiency]

def get_match_level(score):
    if score < 0.25:
        return "Very bad"
    elif score < 0.50:
        return "Bad"
    elif score < 0.75:
        return "Good"
    else:
        return "Very good"

def calculate_skill_match(collaborator, project):
    project_skills = Project_skill.objects.filter(project_role__project = project)
    collaborator_skills = Collaborator_skill.objects.filter(collaborator = collaborator)

    matched_req = 0

    for project_skill in project_skills:
        for collaborator_skill in collaborator_skills:

            skill_matches = collaborator_skill.skill == project_skill.skill
            proficiency_match = proficiency_matching(collaborator_skill.proficiency, project_skill.required_proficiency)

            if skill_matches and proficiency_match:
                matched_req += 1
                break

    total_req = project_skills.count()

    if total_req == 0:
        return 0.0

    return matched_req / total_req

def get_matching_skills(collaborator, project):
    project_skills = Project_skill.objects.filter(project_role__project = project)
    collaborator_skills = Collaborator_skill.objects.filter(collaborator = collaborator)

    matching_skills = []

    for project_skill in project_skills:
        for collaborator_skill in collaborator_skills:
            skill_matches = collaborator_skill.skill == project_skill.skill
            proficiency_match = proficiency_matching(collaborator_skill.proficiency, project_skill.required_proficiency)

        if skill_matches and proficiency_match:
            matching_skills.append(project_skill)
            break

    return matching_skills

def calculate_sector_match(collaborator, project):
    if project.sector in collaborator.sector_interests:
        return 1.0
    else:
        return 0.0

def calculate_commitment_match(collaborator, project):
    if collaborator.commitment == project.commitment:
        return 1.0
    else:
        return 0.0

def calculate_availability_match(collaborator, project):
    project_req_availability = project.req_hours
    collaborator_availability = collaborator.availability

    if collaborator_availability >= project_req_availability:
        return 1.0
    else:
        return collaborator_availability / project_req_availability

def calculate_project_score(collaborator, project, skill_weight = 0.25, availability_weight = 0.25, sector_weight = 0.25, commitment_weight = 0.25):
    skill_match = calculate_skill_match(collaborator, project)
    availability_match = calculate_availability_match(collaborator, project)
    sector_match = calculate_sector_match(collaborator, project)
    commitment_match = calculate_commitment_match(collaborator, project)

    score = (skill_match * skill_weight) + (availability_match * availability_weight) + (sector_match * sector_weight) + (commitment_match * commitment_weight)

    return score

def rank_projects(collaborator):
    projects = Project.objects.all()

    ranked_projects = []

    for project in projects:

        if collaborator.availability < project.req_hours:
            continue

        score = calculate_project_score(collaborator, project)
        match_level = get_match_level(score)
        ranked_projects.append((project, score, match_level))

    ranked_projects.sort(key = itemgetter(1), reverse = True)

    return ranked_projects
