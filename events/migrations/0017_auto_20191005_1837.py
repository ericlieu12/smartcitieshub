# Generated by Django 2.2.6 on 2019-10-05 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_auto_20191005_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='category',
            field=models.CharField(max_length=20),
        ),
    ]
