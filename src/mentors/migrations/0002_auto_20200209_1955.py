# Generated by Django 2.2.4 on 2020-02-09 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='public/mentors/images/'),
        ),
    ]
