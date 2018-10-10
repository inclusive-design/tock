# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-02 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hours', '0041_auto_20180514_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportingperiod',
            name='rendered_message',
            field=models.TextField(blank=True, editable=False, help_text='HTML rendered from Markdown in the message field'),
        ),
        migrations.AddField(
            model_name='timecardnote',
            name='rendered_body',
            field=models.TextField(blank=True, editable=False, help_text='HTML rendered from Markdown in the body field'),
        ),
    ]
