# Generated by Django 2.0.1 on 2019-01-21 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='solution',
            name='corrected',
            field=models.BooleanField(default=False),
        ),
    ]
