# Generated by Django 4.2.5 on 2023-12-02 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0049_transaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='tenant',
        ),
    ]
