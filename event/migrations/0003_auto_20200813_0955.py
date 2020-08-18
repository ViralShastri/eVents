# Generated by Django 3.0.5 on 2020-08-13 04:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20200805_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='EventEndTime',
            field=models.TimeField(default=datetime.datetime(2020, 8, 13, 4, 25, 39, 15924, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='EventStartTime',
            field=models.TimeField(default=datetime.datetime(2020, 8, 13, 4, 25, 39, 15924, tzinfo=utc)),
        ),
    ]