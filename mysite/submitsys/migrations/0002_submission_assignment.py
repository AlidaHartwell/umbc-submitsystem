# Generated by Django 3.0.2 on 2020-02-19 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('submitsys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='assignment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='submitsys.Assignment'),
            preserve_default=False,
        ),
    ]
