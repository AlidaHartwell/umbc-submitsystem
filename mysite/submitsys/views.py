from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template import loader
from django.urls import reverse

from .models import Assignment, Course, Student, Submission, SubmissionFile


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
    course: Course = get_object_or_404(Course, pk=course_id)

    context = {
        "assignments": Assignment.objects.filter(course_fk=course_id),
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


def student_intro(request):
    template = loader. get_template('submitsys/studentintro.html')
    return HttpResponse(template.render({}, request))


def student_login(request):
    return HttpResponseRedirect(reverse('student_console', args=(request.GET['student_id'],)))


def student_console(request, student_id):
    context = {
        'student': Student.objects.get(pk=student_id),
        'courses': Course.objects.all()  # TODO: Only get courses student is enrolled in, many to many field
    }
    template = loader.get_template('submitsys/student.html')
    return HttpResponse(template.render(context, request))
    # response_str = "Hello student " + str(student_id)
    # return HttpResponse(response_str)


def student_assignments(request, student_id, course_id):
    context = {
        'student': Student.objects.get(pk=student_id),
        'course': Course.objects.get(pk=course_id),
        'assignments': Assignment.objects.filter(course_fk=course_id)
    }
    template = loader.get_template('submitsys/student_assignments.html')
    return HttpResponse(template.render(context, request))


def submission_edit(request, student_id, course_id, assignment_id):

    student = Student.objects.get(pk=student_id)
    assignment = Assignment.objects.get(pk=assignment_id)

    try:
        submission = Submission.objects.get(student_fk=student_id, assignment_fk=assignment_id)
    except Submission.DoesNotExist:
        submission = Submission.objects.create(student_fk=student, assignment_fk=assignment)

    try:
        file = SubmissionFile.objects.get(submission_fk=submission.id)
    except SubmissionFile.DoesNotExist:
        file = SubmissionFile.objects.create(submission_fk=submission.id, file_name='examplefilename.txt')

    context = {
        'student': student,
        'course': Course.objects.get(pk=course_id),
        'assignment': assignment,
        'submission': submission,
        'file': file
    }

    template = loader.get_template('submitsys/submission_edit.html')
    return HttpResponse(template.render(context, request))


def submission_save(request, student_id, course_id, assignment_id, submission_id):
    submission = Submission.objects.get(pk=submission_id)
    file = SubmissionFile.objects.filter(submission_fk=submission_id)

    if len(file) == 0:  # This shouldn't ever happen, right? (line102)
        file = SubmissionFile.objects.create(submission_fk=submission, file_name='', file_contents='')
    else:
        file = file[0]

    file.file_name = request.POST['filename']
    file.file_contents = request.POST['filebody']
    file.save()
    return HttpResponseRedirect(reverse('submission_edit', args=[student_id, course_id, assignment_id]))


def course_enroll(request, course_id):
    return HttpResponse("You're trying to enroll students in course %s." % course_id)


def enroll_status(request, course_id):
    return HttpResponse("We are assessing the status of enrollment in course %s." % course_id)
