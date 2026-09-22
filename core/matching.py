from .models import Collaborator_skill, Project_skill

proficiency_levels = {
    "beginner": 1, 
    "intermediate": 2, 
    "advanced": 3, 
    "expert": 4
    }

def proficiency_matching(collaborator_proficiency, required_proficiency):
    return proficiency_levels[collaborator_proficiency] >= proficiency_levels[required_proficiency]

def calculate_skill_match(collaborator, project):
    project_skills = Project_skill.objects.filter(project = project)
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