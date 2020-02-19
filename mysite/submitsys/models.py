from django.db import models


# Create your models here.
class Assignment(models.Model):
    assignment_name = models.CharField(max_length=15, primary_key=True, default='HW0')


class Student(models.Model):
    student_id = models.CharField(max_length=7, primary_key=True, default='NK16856')
    student_email = models.CharField(max_length=30)

    def __str__(self):
        return self.student_id

class Submission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, default='HW0')
    file_name = models.CharField(max_length=15)

    def __str__(self):
        return self.file_name

