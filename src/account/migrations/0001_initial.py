from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Deadline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deadline', models.DateTimeField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('DT', 'DevTeam'), ('NET', 'NeTeam'), ('ST', 'SecurITeam'), ('SYS', 'SysAdmin'), ('HAT', 'Hallgatói Tudásbázis'), ('N', 'None')], default='N', max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_date', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('motivation_about', models.TextField(blank=True, default='')),
                ('motivation_profession', models.TextField(blank=True, default='')),
                ('motivation_exercise', models.TextField(blank=True, default='')),
                ('nick', models.CharField(blank=True, default='', max_length=15)),
                ('signed', models.BooleanField(default=False)),
                ('role', models.CharField(choices=[('Staff', 'Staff'), ('Applicant', 'Applicant'), ('Student', 'Student')], default='Applicant', max_length=10)),
                ('groups', models.ManyToManyField(blank=True, related_name='profiles', to='account.GroupChoice')),
            ]
        ),
    ]
