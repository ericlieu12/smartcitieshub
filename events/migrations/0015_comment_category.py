# Generated by Django 2.2.6 on 2019-10-05 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_auto_20191005_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='category',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]