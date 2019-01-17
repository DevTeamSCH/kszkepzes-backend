import common.middleware
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('note', models.TextField(blank=True, default='')),
                ('accepted', models.BooleanField()),
                ('corrected', models.BooleanField()),
                ('created_by', models.ForeignKey(default=common.middleware.CurrentUserMiddleware.get_current_user_profile, on_delete=django.db.models.deletion.DO_NOTHING, related_name='solution', to='account.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=150)),
                ('text', models.TextField()),
                ('deadline', models.DateTimeField()),
                ('created_by', models.ForeignKey(default=common.middleware.CurrentUserMiddleware.get_current_user_profile, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tasks', to='account.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='solution',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solutions', to='homework.Task'),
        ),
    ]
