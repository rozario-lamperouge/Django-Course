# Generated by Django 3.0.6 on 2020-06-29 14:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='bgimg',
            field=models.CharField(default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 29, 20, 26, 7, 982523)),
        ),
    ]
