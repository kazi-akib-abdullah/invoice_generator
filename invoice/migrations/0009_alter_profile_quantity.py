# Generated by Django 3.2.4 on 2021-06-20 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0008_profile_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
