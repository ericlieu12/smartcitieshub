# Generated by Django 2.2.6 on 2019-10-05 13:18

from django.db import migrations
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20191005_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='geolocation',
            field=django_google_maps.fields.GeoLocationField(default='lat = 1, lon = 2)', max_length=100),
        ),
    ]
