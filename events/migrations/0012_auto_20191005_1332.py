# Generated by Django 2.2.6 on 2019-10-05 13:32

from django.db import migrations
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20191005_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='address',
            field=django_google_maps.fields.AddressField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='comment',
            name='geolocation',
            field=django_google_maps.fields.GeoLocationField(default='', max_length=100),
        ),
    ]
