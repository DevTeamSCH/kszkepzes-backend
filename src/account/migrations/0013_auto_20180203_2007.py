# Generated by Django 2.0.1 on 2018-02-03 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20180125_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='join_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]