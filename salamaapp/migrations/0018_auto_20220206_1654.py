# Generated by Django 3.2.7 on 2022-02-06 15:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salamaapp', '0017_auto_20220205_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 6, 16, 54, 53, 777155)),
        ),
        migrations.AlterField(
            model_name='youthpost',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 6, 16, 54, 53, 776154)),
        ),
    ]