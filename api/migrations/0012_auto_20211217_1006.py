# Generated by Django 3.2.10 on 2021-12-17 10:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_reservation_expiry_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seat',
            name='row',
        ),
        migrations.RemoveField(
            model_name='seat',
            name='section',
        ),
        migrations.AlterField(
            model_name='reservation',
            name='expiry_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 17, 10, 21, 34, 62512)),
        ),
    ]
