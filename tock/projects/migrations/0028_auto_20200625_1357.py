# Generated by Django 2.2.13 on 2020-06-25 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0027_project_include_in_utilization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='include_in_utilization',
            field=models.BooleanField(default=False, help_text='For handling microrequests, per github.com/18F/tock/issues/1084'),
        ),
    ]
