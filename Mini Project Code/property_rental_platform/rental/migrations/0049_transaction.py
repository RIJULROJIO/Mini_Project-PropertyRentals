# Generated by Django 4.2.5 on 2023-12-02 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0048_delete_transaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('security_deposit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(default='INR', max_length=3)),
                ('order_id', models.CharField(max_length=255)),
                ('payment_id', models.CharField(blank=True, max_length=255, null=True)),
                ('payment_status', models.CharField(blank=True, max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.property')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.profile')),
            ],
        ),
    ]
