# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-21 16:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relearn_research', '0003_auto_20161221_1621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='information',
            old_name='summary',
            new_name='description',
        ),
    ]
