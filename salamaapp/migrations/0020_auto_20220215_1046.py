# Generated by Django 3.2.7 on 2022-02-15 09:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salamaapp', '0019_auto_20220215_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 15, 10, 46, 13, 277277)),
        ),
        migrations.AlterField(
            model_name='youthpost',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 15, 10, 46, 13, 275278)),
        ),
    ]