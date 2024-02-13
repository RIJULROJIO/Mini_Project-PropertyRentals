# Generated by Django 4.2.5 on 2024-02-12 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0081_delete_serviceproviderprofile_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceProviderProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('business_name', models.CharField(max_length=200)),
                ('experience', models.IntegerField(blank=True, null=True)),
                ('certification_file', models.FileField(upload_to='certifications/')),
                ('address', models.TextField()),
                ('approved', models.BooleanField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
