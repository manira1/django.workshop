# Generated by Django 2.0.6 on 2018-06-13 10:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20180613_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielist',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 13, 10, 53, 34, 952693, tzinfo=utc)),
        ),
    ]
