# Generated by Django 2.0.1 on 2018-05-28 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0017_auto_20180205_2004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('file', models.FileField(upload_to='')),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.Profile')),
            ],
        ),
    ]
