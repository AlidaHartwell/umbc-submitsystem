from django.db import models


# Create your models here.
class Assignment(models.Model):
    assignment_name = models.CharField(max_length=15, default='HW0')


class Student(models.Model):
    student_id = models.CharField(max_length=7, default='NULL')
    student_email = models.CharField(max_length=30)

    def __str__(self):
        return self.student_id


class Submission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=15)
    mongo_db = models.CharField(max_length=512, default="NULL")

    def __str__(self):
        return self.file_name
