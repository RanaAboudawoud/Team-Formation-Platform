from django.http import HttpResponse

def home(request):
    return HttpResponse("Team Formation Platform")
