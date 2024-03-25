# Generated by Django 4.2.5 on 2024-03-20 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0134_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertysell',
            name='verification_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('verified', 'Verified'), ('rejected', 'Rejected')], default='pending', max_length=20),
        ),
    ]
