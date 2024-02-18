# Generated by Django 4.2.5 on 2024-02-17 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0093_delete_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=255, null=True)),
                ('service_category', models.CharField(max_length=255, null=True)),
                ('property_type', models.CharField(max_length=255, null=True)),
                ('service_description', models.TextField(null=True)),
                ('service_price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('location', models.CharField(max_length=255, null=True)),
                ('service_provider_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.serviceproviderprofile')),
            ],
        ),
    ]
