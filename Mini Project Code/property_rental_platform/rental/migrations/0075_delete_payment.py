# Generated by Django 4.2.5 on 2024-02-12 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0074_payment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]