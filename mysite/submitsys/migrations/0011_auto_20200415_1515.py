# Generated by Django 3.0.2 on 2020-04-15 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submitsys', '0010_student_student_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissionfile',
            name='file_name',
            field=models.CharField(default='NULL', max_length=80),
        ),
    ]