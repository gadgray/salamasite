# Generated by Django 3.2.7 on 2022-02-15 10:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salamaapp', '0023_auto_20220215_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 15, 11, 14, 57, 821292)),
        ),
        migrations.AlterField(
            model_name='pastorscorner',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 15, 11, 14, 57, 823290)),
        ),
        migrations.AlterField(
            model_name='youthpost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 15, 11, 14, 57, 820291)),
        ),
    ]
