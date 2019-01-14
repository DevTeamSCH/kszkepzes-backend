# Generated by Django 2.0.1 on 2019-01-13 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0003_auto_20190107_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='stats.Event'),
        ),
        migrations.AlterField(
            model_name='note',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='account.Profile'),
        ),
    ]