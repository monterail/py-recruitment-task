# Generated by Django 3.2.10 on 2021-12-18 10:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_alter_reservation_expiry_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='expiry_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 18, 10, 54, 6, 41389)),
        ),
    ]