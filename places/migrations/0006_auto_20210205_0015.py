# Generated by Django 3.0.7 on 2021-02-04 21:15

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_auto_20210204_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='description_long',
            field=tinymce.models.HTMLField(default='Подробное описание'),
        ),
    ]
