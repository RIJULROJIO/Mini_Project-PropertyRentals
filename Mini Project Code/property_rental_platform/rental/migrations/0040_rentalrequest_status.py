# Generated by Django 4.2.5 on 2023-11-25 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0039_remove_rentalrequest_approval_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentalrequest',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=20),
        ),
    ]
