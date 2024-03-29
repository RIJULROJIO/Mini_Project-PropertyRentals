# Generated by Django 4.2.5 on 2024-02-17 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0089_delete_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razorpay_payment_id', models.CharField(max_length=255)),
                ('razorpay_order_id', models.CharField(max_length=255)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.property')),
            ],
        ),
    ]
