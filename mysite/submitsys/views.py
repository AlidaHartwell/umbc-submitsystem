from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Assignment, Course


def index(request):
    return HttpResponse("Welcome to the UMBC CMSC Submit System!")


def course_console(request):
    context = {
        "courses": Course.objects.all(),
    }
    template = loader.get_template('submitsys/course.html')
    return HttpResponse(template.render(context, request))


def course_create(request):
    course = Course.objects.create(course_name=request.POST['courseName'])
    course.save()
    return HttpResponseRedirect(reverse('course_console'))


def assignment_console(request, course_id):
    context = {
        "assignments": Assignment.objects.all(),
        "course_id": course_id,
    }
    template = loader.get_template('submitsys/assignment.html')
    return HttpResponse(template.render(context, request))


def assignment_create(request, course_id):
    assignment = Assignment.objects.create(assignment_name=request.POST['assignmentName'],
                                           course_fk=Course.objects.get(pk=course_id),
                                           point_value=0)
    assignment.save()
    return HttpResponseRedirect(reverse('assignment_console'))


def detail(request, assignment_id):
    return HttpResponse("You're looking at assignment %s." % assignment_id)


def student(request, assignment_id):
    response = "You're viewing the submission for assignment %s"
    return HttpResponse(response % assignment_id)
