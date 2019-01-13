# Generated by Django 2.0.1 on 2019-01-07 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='event',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='stats.Event'),
        ),
        migrations.AlterField(
            model_name='note',
            name='profile',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='account.Profile'),
        ),
    ]
