# Generated by Django 3.0.7 on 2021-02-01 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='details_url',
            field=models.TextField(default='ссылка на подробности'),
        ),
    ]