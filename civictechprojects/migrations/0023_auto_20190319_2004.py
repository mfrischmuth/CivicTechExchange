# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-03-19 20:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('civictechprojects', '0022_auto_20190211_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteerrelation',
            name='re_enroll_last_reminder_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='volunteerrelation',
            name='re_enroll_reminder_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='volunteerrelation',
            name='re_enrolled_last_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='volunteerrelation',
            name='approved_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='volunteerrelation',
            name='last_reminder_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='volunteerrelation',
            name='projected_end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
