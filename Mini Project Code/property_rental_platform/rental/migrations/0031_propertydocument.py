# Generated by Django 4.2.5 on 2023-11-11 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0030_property_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.CharField(max_length=50)),
                ('document', models.FileField(upload_to='property_documents/')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='rental.property')),
            ],
        ),
    ]
