from django.http import HttpResponse
from django.template import loader


def index(request):
    return HttpResponse("Welcome to the UMBC CMSC Submit System!")


def assignment_console(request):
    context = {

    }
    template = loader.get_template('submitsys/assignment.html')
    return HttpResponse(template.render(context, request))


def assignment_create(request):
    return HttpResponse("we did it:  " + request.POST['assignmentName'])


def detail(request, assignment_id):
    return HttpResponse("You're looking at assignment %s." % assignment_id)


def student(request, assignment_id):
    response = "You're viewing the submission for assignment %s"
    return HttpResponse(response % assignment_id)
