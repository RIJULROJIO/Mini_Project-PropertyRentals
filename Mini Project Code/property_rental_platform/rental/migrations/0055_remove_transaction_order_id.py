# Generated by Django 4.2.5 on 2023-12-02 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0054_transaction_security_deposit_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='order_id',
        ),
    ]
