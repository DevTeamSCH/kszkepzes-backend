# Generated by Django 2.0.1 on 2018-04-04 06:53

import common.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0010_auto_20180404_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='files',
            field=models.FileField(blank=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(['image/png', 'image/jpeg', 'application/zip']), common.validators.FileSizeValidator(size_limit=52428800)]),
        ),
        migrations.AlterField(
            model_name='task',
            name='files',
            field=models.FileField(blank=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(['image/png', 'image/jpeg', 'application/zip']), common.validators.FileSizeValidator(size_limit=52428800)]),
        ),
    ]
