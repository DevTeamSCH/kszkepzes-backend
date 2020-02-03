# Generated by Django 2.2.4 on 2020-02-02 23:16

import common.validators
import django.core.validators
from django.db import migrations, models
import document.models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0005_auto_20190129_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=document.models.document_file_name, validators=[django.core.validators.FileExtensionValidator(['png', 'jpeg', 'jpg', 'zip']), common.validators.FileSizeValidator(size_limit=52428800)]),
        ),
    ]
