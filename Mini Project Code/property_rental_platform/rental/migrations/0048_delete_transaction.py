# Generated by Django 4.2.5 on 2023-12-02 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0047_remove_property_in_cart'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]
