# Generated by Django 3.2.7 on 2021-12-22 11:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salamaapp', '0009_auto_20211221_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youthpost',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
