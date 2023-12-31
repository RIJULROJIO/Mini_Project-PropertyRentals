# Generated by Django 4.2.5 on 2023-11-01 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0010_delete_propertyimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='property_images/')),
                ('category', models.CharField(max_length=50)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.property')),
            ],
        ),
    ]
