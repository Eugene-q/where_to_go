# Generated by Django 3.0.7 on 2021-02-01 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_location_details_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='details_url',
        ),
    ]