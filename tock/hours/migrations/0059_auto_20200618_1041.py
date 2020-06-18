# Generated by Django 2.2.13 on 2020-06-18 14:41

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hours', '0058_auto_20200512_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timecard',
            name='billable_expectation',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.8000000000000000444089209850062616169452667236328125'), max_digits=3, validators=[django.core.validators.MaxValueValidator(limit_value=1)], verbose_name='Percent hours billable per week'),
        ),
    ]
