# Generated by Django 3.2.7 on 2022-02-05 16:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salamaapp', '0012_uploads'),
    ]

    operations = [
        migrations.DeleteModel(
            name='banner',
        ),
        migrations.AddField(
            model_name='uploads',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='youthpost',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 5, 17, 34, 31, 447060)),
        ),
    ]