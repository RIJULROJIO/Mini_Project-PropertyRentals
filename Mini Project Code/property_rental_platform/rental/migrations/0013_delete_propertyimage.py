# Generated by Django 4.2.5 on 2023-11-01 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0012_alter_propertyimage_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PropertyImage',
        ),
    ]