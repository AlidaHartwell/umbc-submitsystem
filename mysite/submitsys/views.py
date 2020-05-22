import csv

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from datetime import datetime, timezone

from .models import Assignment, Course, Student, Submission, SubmissionFile


def index(request):
    template = loader.get_template("submitsys/index.html")
    return HttpResponse(template.render({}, request))


def course_console(request):

    courses = Course.objects.all()
    assignments = []

    for course in courses:
        course_assignments = Assignment.objects.filter(course_fk=course.id)
        for assignment in course_assignments:
            if assignment.due_date > datetime.now(timezone.utc):
                assignments.append(assignment)

    context = {
        "courses": courses,
        "assignments": assignments,
    }
    template = loader.get_template('submitsys/course_dashboard.html')
    return HttpResponse(template.render(context, request))


def course_create(request):
    course = Course.objects.create(course_name=request.POST['courseName'])
    course.save()
    return HttpResponseRedirect(reverse('course_console'))


def assignment_console(request, course_id): # TODO: Link to a new view with all submissions
    course: Course = get_object_or_404(Course, pk=course_id)

    context = {
        "assignments": Assignment.objects.filter(course_fk=course_id),
        "course_id": course_id,
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
    template = loader.get_template('submitsys/studentintro.html')
    return HttpResponse(template.render({}, request))


def student_login(request):
    return HttpResponseRedirect(reverse('student_console', args=(request.GET['student_id'],)))


def student_console(request, student_id):
    student = Student.objects.get(pk=student_id)
    courses = student.student_courses.all()
    assignments = []

    for course in courses:
        course_assignments = Assignment.objects.filter(course_fk=course.id)
        for assignment in course_assignments:
            if assignment.due_date > datetime.now(timezone.utc):
                assignments.append(assignment)

    context = {
        'student': student,
        'courses': courses,
        'assignments': assignments
    }
    template = loader.get_template('submitsys/student_console.html')
    return HttpResponse(template.render(context, request))


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

    files = SubmissionFile.objects.filter(submission_fk=submission.id)

    context = {
        'student': student,
        'course': Course.objects.get(pk=course_id),
        'assignment': assignment,
        'submission': submission,
        'files': files
    }

    template = loader.get_template('submitsys/submission_edit.html')
    return HttpResponse(template.render(context, request))


def submission_file_save(request, student_id, course_id, assignment_id, submission_id):
    submission = Submission.objects.get(pk=submission_id)
    file = SubmissionFile.objects.filter(submission_fk=submission_id)
    student = Student.objects.get(pk=student_id)

    if submission.student_fk == student:

        if len(file) == 0:
            file = SubmissionFile.objects.create(submission_fk=submission, file_name='', file_contents='')
        else:
            file = file[0]

        file.file_name = request.POST['filename']
        file.file_contents = request.POST['filebody']
        file.save()

    return HttpResponseRedirect(reverse('submission_edit', args=[student_id, course_id, assignment_id]))


def submission_file_create(request, student_id, course_id, assignment_id, submission_id):
    submission = Submission.objects.get(pk=submission_id)
    file = SubmissionFile(submission_fk=submission)

    with open(request.POST['fileUpload']) as f:
        file.file_contents = f.read()
        file.file_name = request.POST['fileUpload']

    file.save()
    return HttpResponseRedirect(reverse('submission_edit', args=[student_id, course_id, assignment_id]))


def new_enrollment(request, course_id):

    context = {
        'course': Course.objects.get(pk=course_id)
    }
    template = loader.get_template('submitsys/new_enrollment.html')
    return HttpResponse(template.render(context, request))


def course_enrollment(request, course_id):
    with open(request.POST['student_upload']) as file:
        reader = csv.reader(file)
        for row in reader:
            student, created = Student.objects.get_or_create(
                student_num=row[0],
                student_email=row[1]
            )
            student.save()
            student.student_courses.add(Course.objects.get(pk=course_id))
    return HttpResponseRedirect(reverse("new_enrollment", args=[course_id]))


def single_enrollment(request, course_id):
    course: Course = get_object_or_404(Course, pk=course_id)
    return render(request, 'submitsys/add_single.html', context={'course': course})

def save_single_enrollment(request, course_id):
    course: Course = get_object_or_404(Course, pk=course_id)
    student: Student
    student, created = Student.objects.get_or_create(student_email=request.POST['email'])
    student.student_fname = request.POST['firstname']
    student.student_lname = request.POST['lastname']
    student.student_courses.add(course)
    student.save()
    return HttpResponseRedirect(reverse('assignment_console', args=[course_id]))