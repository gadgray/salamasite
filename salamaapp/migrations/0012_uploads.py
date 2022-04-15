# Generated by Django 3.2.7 on 2022-02-05 15:05

from django.db import migrations, models
import salamaapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('salamaapp', '0011_banner_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='uploads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('file', models.FileField(blank=True, null=True, upload_to=salamaapp.models.filepath)),
            ],
        ),
    ]
