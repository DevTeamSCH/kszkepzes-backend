import common.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('homework', '0001_initial'),
        ('account', '0001_initial'),
        ('homework', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, default='')),
                ('file', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(['png', 'jpeg', 'jpg', 'zip']), common.validators.FileSizeValidator(size_limit=52428800)])),
                ('solution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='files', to='homework.Solution')),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.Profile')),
            ],
        ),
    ]
