# Generated by Django 4.2.5 on 2023-12-03 02:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0059_transaction'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]
