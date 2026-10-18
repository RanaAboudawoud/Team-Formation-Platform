from .models import Project_interest

def get_interested_collaborators(project):
    interests = Project_interest.objects.filter(project = project)

    collaborators = []

    for interest in interests:
        collaborators.append(interest.collaborator)

    return collaborators