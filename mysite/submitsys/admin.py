from django.contrib import admin
from .models import Assignment, Course, Student, Rubric, Submission

# Register your models here.
admin.site.register(Assignment)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Rubric)
admin.site.register(Submission)