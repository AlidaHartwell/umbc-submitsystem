from django.contrib import admin
from .models import Assignment, Course, Student, Rubric, Submission, SubmissionFile

# Register your models here.
admin.site.register(Assignment)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Rubric)
admin.site.register(Submission)
admin.site.register(SubmissionFile)