# Generated by Django 3.2.7 on 2021-11-25 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salamaapp', '0002_progarms'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='progarms',
            new_name='Program',
        ),
        migrations.RenameField(
            model_name='program',
            old_name='createdOn',
            new_name='date',
        ),
    ]
