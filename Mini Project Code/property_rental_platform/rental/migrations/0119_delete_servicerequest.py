# Generated by Django 4.2.5 on 2024-03-01 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0118_servicerequest_schedule_date_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ServiceRequest',
        ),
    ]