# Generated by Django 3.2.10 on 2021-12-19 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0046_remove_transaction_total_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(choices=[('GBP', 'GBP'), ('OTHER', 'OTHER')], default='GBP', max_length=100)),
                ('token', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.reservation')),
            ],
        ),
    ]
