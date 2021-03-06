# Generated by Django 3.2.4 on 2021-06-20 11:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0003_auto_20210619_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='product_details',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 20, 11, 43, 48, 385451, tzinfo=utc), editable=False),
        ),
    ]
