# Generated by Django 4.2.5 on 2024-03-01 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0112_remove_servicerequest_scheduled_date_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ServiceRequest',
        ),
    ]
