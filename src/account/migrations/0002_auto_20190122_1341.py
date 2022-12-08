# Generated by Django 2.0.1 on 2019-01-22 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('Staff', 'Staff'), ('Applicant', 'Applicant'), ('Student', 'Student'), ('Denied', 'Denied')], default='Applicant', max_length=10),
        ),
    ]