# Generated by Django 2.2.12 on 2020-05-07 20:04

from django.conf import settings
import django.core.validators
from django.db import migrations, models

def backfill_expected_billable_hours(apps, schema_editor):
    UserData = apps.get_model('employees', 'UserData')

    for user_data in UserData.objects.all():
        user_data.expected_billable_hours = round(user_data.billable_expectation * settings.HOURS_IN_A_REGULAR_WORK_WEEK)
        user_data.save()

class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0030_auto_20200505_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='expected_billable_hours',
            field=models.IntegerField(default=32, help_text='Number of hours expected to be billable each week', validators=[django.core.validators.MaxValueValidator(limit_value=40)]),
        ),
    ]
