# Generated by Django 3.0.2 on 2020-04-15 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submitsys', '0009_auto_20200409_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_courses',
            field=models.ManyToManyField(to='submitsys.Course'),
        ),
    ]
