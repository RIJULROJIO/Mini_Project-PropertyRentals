# Generated by Django 4.2.5 on 2023-09-23 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='confirmpassword',
            field=models.CharField(default='', max_length=100),
        ),
    ]
