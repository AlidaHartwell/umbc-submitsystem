from django.db import models


# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=8, default='CMSC 201')


class Assignment(models.Model):
    assignment_name = models.CharField(max_length=15, default='HW0')
    course_fk = models.ForeignKey(Course, on_delete=models.CASCADE)
    point_value = models.IntegerField()


class Student(models.Model):
    student_id = models.CharField(max_length=7, default='NULL')
    student_email = models.CharField(max_length=30)

    def __str__(self):
        return self.student_id


class Submission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=15)
    assignment_fk = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    mongo_db = models.CharField(max_length=512, default="NULL")

    def __str__(self):
        return self.file_name

