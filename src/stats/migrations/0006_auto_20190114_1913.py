# Generated by Django 2.0.1 on 2019-01-14 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0005_auto_20190114_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='visitors',
            field=models.ManyToManyField(blank=True, related_name='events', to='account.Profile'),
        ),
    ]
