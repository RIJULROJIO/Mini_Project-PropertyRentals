# Generated by Django 4.2.5 on 2024-02-27 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0108_message'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
    ]