# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-23 16:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20180123_1713'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groupchoice',
            old_name='pref_group',
            new_name='choice',
        ),
        migrations.AlterUniqueTogether(
            name='groupchoice',
            unique_together=set([('choice', 'profile')]),
        ),
    ]