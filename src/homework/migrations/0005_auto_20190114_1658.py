# Generated by Django 2.0.1 on 2019-01-14 15:58

import common.middleware
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0004_auto_20190114_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solutions', to='homework.Task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_by',
            field=models.ForeignKey(default=common.middleware.CurrentUserMiddleware.get_current_user_profile, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tasks', to='account.Profile'),
        ),
    ]