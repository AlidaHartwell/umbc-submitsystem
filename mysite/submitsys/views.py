from django.http import HttpResponse
from .models import Assignment, Student, Submission


def index(request):
    return HttpResponse("Welcome to the UMBC CMSC Submit System!")


def detail(request, assignment_id):
    return HttpResponse("You're looking at assignment %s." % assignment_id)


def student(request, assignment_id):
    response = "You're viewing the submission for assignment %s"
    return HttpResponse(response % assignment_id)