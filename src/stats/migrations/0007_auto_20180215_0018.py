# Generated by Django 2.0.1 on 2018-02-14 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0006_auto_20180214_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='visitors',
            field=models.ManyToManyField(related_name='visitor', to='account.Profile'),
        ),
    ]
