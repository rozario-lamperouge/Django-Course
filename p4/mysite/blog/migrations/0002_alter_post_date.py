# Generated by Django 4.1.6 on 2023-02-13 20:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 2, 14, 2, 20, 16, 183583)
            ),
        ),
    ]
