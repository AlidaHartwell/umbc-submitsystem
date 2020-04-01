from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Assignment, Course, Student


def index(request):
    template = loader.get_template("submitsys/index.html")
    return HttpResponse(template.render({}, request))


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
        "assignments": Assignment.objects.all(),  # TODO: Get all assignments for course ID
        "course_id": course_id,  # Get course object with course ID -> how do access model info from DB
    }
    template = loader.get_template('submitsys/assignment.html')
    return HttpResponse(template.render(context, request))


def assignment_create(request, course_id):
    assignment = Assignment.objects.create(assignment_name=request.POST['assignmentTitle'],
                                           course_fk=Course.objects.get(pk=course_id),
                                           point_value=0)
    assignment.save()
    return HttpResponseRedirect(reverse('assignment_console', args=(course_id,)))


def assignment_form(request, course_id):  # Will be a form to input assignment name, pt vals, upload rubric
    context = {
        "course_id": course_id,
    }
    template = loader.get_template('submitsys/assignment_form.html')
    return HttpResponse(template.render(context, request))


def detail(request, assignment_id):
    return HttpResponse("You're looking at assignment %s." % assignment_id)


def student_console(request, student_id):
    context = {
        'student': Student.objects.get(pk=student_id),
        'courses': Course.objects.all()
    }
    template = loader.get_template('submitsys/student.html')
    return HttpResponse(template.render(context, request))
    # response_str = "Hello student " + str(student_id)
    # return HttpResponse(response_str)


def student_courses(request, student_id, course_id):
    response_str = "Hello student " + str(student_id) + "! You are viewing course " + str(course_id)
    return HttpResponse(response_str)


def assignment_submissions(request, student_id, course_id, assignment_id):
    response_str = "Hello student " + str(student_id) + "! You are viewing course " + str(
        course_id) + " and assignment " + str(assignment_id)
    return HttpResponse(response_str)


def course_enroll(request, course_id):
    return HttpResponse("You're trying to enroll in course %s." % course_id)


def enroll_status(request, course_id):
    return HttpResponse("We are assessing the status of your enrollment in course %s." % course_id)
