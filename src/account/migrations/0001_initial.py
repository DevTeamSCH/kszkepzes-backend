# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-11 14:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_date', models.DateField()),
                ('pref_group', models.CharField(choices=[('DT', 'DevTeam'), ('NET', 'NeTeam'), ('ST', 'SecurITeam'), ('SYS', 'SysAdmin'), ('N', 'None')], default='None', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]