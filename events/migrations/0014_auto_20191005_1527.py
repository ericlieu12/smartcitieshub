# Generated by Django 2.2.6 on 2019-10-05 15:27

from django.db import migrations
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_auto_20191005_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='address',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='geolocation',
        ),
        migrations.AddField(
            model_name='post',
            name='address',
            field=django_google_maps.fields.AddressField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='geolocation',
            field=django_google_maps.fields.GeoLocationField(default='', max_length=100),
        ),
    ]
