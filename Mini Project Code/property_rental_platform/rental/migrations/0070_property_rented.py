# Generated by Django 4.2.5 on 2024-02-11 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0069_delete_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='rented',
            field=models.BooleanField(default=False),
        ),
    ]
