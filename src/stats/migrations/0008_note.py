# Generated by Django 2.0.1 on 2018-02-21 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_auto_20180205_2004'),
        ('stats', '0007_auto_20180215_0018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_notes', to='account.Profile')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='stats.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='account.Profile')),
            ],
        ),
    ]
