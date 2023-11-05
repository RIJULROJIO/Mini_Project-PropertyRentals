# Generated by Django 4.2.5 on 2023-11-04 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0018_remove_amenity_balcony_remove_amenity_parking_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='amenity',
            name='balcony',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=3),
        ),
        migrations.AddField(
            model_name='amenity',
            name='parking_area',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=3),
        ),
    ]
