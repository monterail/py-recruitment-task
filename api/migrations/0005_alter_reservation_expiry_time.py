# Generated by Django 3.2.10 on 2021-12-16 23:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20211216_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='expiry_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 16, 23, 48, 7, 766913)),
        ),
    ]
