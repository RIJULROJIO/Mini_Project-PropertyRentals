# Generated by Django 4.2.5 on 2024-02-07 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0062_serviceproviderprofile_alter_notification_sender_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ServiceProviderProfile',
        ),
    ]