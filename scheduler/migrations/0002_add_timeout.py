# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 01:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='repeatablejob',
            name='timeout',
            field=models.IntegerField(blank=True, help_text="Timeout specifies the maximum runtime, in seconds, for the job before it'll be considered 'lost'. Blank uses the default timeout.", null=True, verbose_name='timeout'),  # noqa
        ),
        migrations.AddField(
            model_name='scheduledjob',
            name='timeout',
            field=models.IntegerField(blank=True, help_text="Timeout specifies the maximum runtime, in seconds, for the job before it'll be considered 'lost'. Blank uses the default timeout.", null=True, verbose_name='timeout'),  # noqa
        ),
    ]