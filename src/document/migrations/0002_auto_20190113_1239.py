# Generated by Django 2.0.1 on 2019-01-13 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='files',
            new_name='file',
        ),
    ]