# Generated by Django 2.2.5 on 2020-09-04 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20200902_1904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='romm',
            new_name='room',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='adress',
            new_name='address',
        ),
    ]
