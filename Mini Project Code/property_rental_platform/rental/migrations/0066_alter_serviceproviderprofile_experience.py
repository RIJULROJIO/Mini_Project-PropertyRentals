# Generated by Django 4.2.5 on 2024-02-07 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0065_alter_serviceproviderprofile_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceproviderprofile',
            name='experience',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]