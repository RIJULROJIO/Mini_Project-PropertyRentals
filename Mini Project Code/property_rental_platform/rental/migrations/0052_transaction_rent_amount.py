# Generated by Django 4.2.5 on 2023-12-02 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0051_remove_transaction_rent_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='rent_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
