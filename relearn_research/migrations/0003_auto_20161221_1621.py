# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-21 16:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relearn_research', '0002_auto_20161108_0310'),
    ]

    operations = [
        migrations.RenameField(
            model_name='information',
            old_name='link',
            new_name='url',
        ),
        migrations.RenameField(
            model_name='website',
            old_name='link',
            new_name='url',
        ),
    ]
