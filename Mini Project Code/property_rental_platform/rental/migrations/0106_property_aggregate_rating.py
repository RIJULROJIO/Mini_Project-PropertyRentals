# Generated by Django 4.2.5 on 2024-02-27 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0105_propertyfeedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='aggregate_rating',
            field=models.FloatField(default=0.0),
        ),
    ]