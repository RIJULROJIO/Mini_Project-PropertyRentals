# Generated by Django 4.2.5 on 2024-02-08 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0066_alter_serviceproviderprofile_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceproviderprofile',
            name='approved',
            field=models.BooleanField(null=True),
        ),
    ]