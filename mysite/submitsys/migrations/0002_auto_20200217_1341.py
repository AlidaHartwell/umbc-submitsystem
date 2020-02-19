# Generated by Django 3.0.2 on 2020-02-17 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('submitsys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('assignment_name', models.CharField(default='HW0', max_length=15, primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AddField(
            model_name='student',
            name='student_id',
            field=models.CharField(default='NK16856', max_length=7, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='submission',
            name='assignment',
            field=models.ForeignKey(default='HW0', on_delete=django.db.models.deletion.CASCADE, to='submitsys.Assignment'),
        ),
    ]
