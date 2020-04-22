from django.db import models
import datetime


# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=8, default='Course Name')

    def __str__(self):
        return self.course_name


class Assignment(models.Model):
    assignment_name = models.CharField(max_length=15, default='HW0')
    course_fk = models.ForeignKey(Course, on_delete=models.CASCADE)
    point_value = models.IntegerField()
    due_date = models.DateTimeField(default=datetime.datetime.now() + datetime.timedelta(weeks=2))

    def __str__(self):
        return self.assignment_name


class Rubric(models.Model):
    assignment_fk = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    is_blank = models.BooleanField(default=True)


class RubricSection(models.Model):
    rubric_fk = models.ForeignKey(Rubric, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000, default="General")


class RubricItem(models.Model):
    section_fk = models.ForeignKey(RubricSection, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000, default="")
    possible_points = models.IntegerField()
    is_optional = models.BooleanField()


class Student(models.Model):
    student_fname = models.TextField(default='NULL')
    student_lname = models.TextField(default='NULL')
    student_num = models.CharField(max_length=7, default='NULL')
    student_email = models.CharField(max_length=30)
    student_courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.student_fname + " " + self.student_lname


class Submission(models.Model):
    student_fk = models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment_fk = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    mongo_db = models.CharField(max_length=512, default="NULL")


class SubmissionFile(models.Model):
    file_name = models.CharField(max_length=80, default="NULL")
    file_contents = models.TextField(default="NULL")
    submission_fk = models.ForeignKey(Submission, on_delete=models.CASCADE)

    def __str__(self):
        return self.file_name
