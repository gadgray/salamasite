# Generated by Django 3.2.7 on 2022-02-05 21:42

import datetime
from django.db import migrations, models
import salamaapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('salamaapp', '0016_auto_20220205_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='audioMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.FileField(null=True, upload_to=salamaapp.models.filepath)),
            ],
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 5, 22, 42, 17, 759279)),
        ),
        migrations.AlterField(
            model_name='youthpost',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 5, 22, 42, 17, 758280)),
        ),
    ]
