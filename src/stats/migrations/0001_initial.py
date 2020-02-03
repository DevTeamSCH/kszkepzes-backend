# Generated by Django 2.0.1 on 2019-01-17 15:06

import common.middleware
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(default=common.middleware.CurrentUserMiddleware.get_current_user_profile,
                                                 on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_event', to='account.Profile')),
                ('visitors', models.ManyToManyField(blank=True,
                                                    related_name='events', to='account.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(default=common.middleware.CurrentUserMiddleware.get_current_user_profile,
                                                 on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_notes', to='account.Profile')),
                ('event', models.ForeignKey(blank=True, null=True,
                                            on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='stats.Event')),
                ('profile', models.ForeignKey(blank=True, null=True,
                                              on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='account.Profile')),
            ],
        ),
    ]
