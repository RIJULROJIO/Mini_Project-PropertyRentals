# Generated by Django 4.2.5 on 2023-12-02 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0055_remove_transaction_order_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]
