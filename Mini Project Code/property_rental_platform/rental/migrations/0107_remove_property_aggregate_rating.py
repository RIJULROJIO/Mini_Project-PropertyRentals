# Generated by Django 4.2.5 on 2024-02-27 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0106_property_aggregate_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='aggregate_rating',
        ),
    ]
