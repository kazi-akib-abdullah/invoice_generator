# Generated by Django 3.2.4 on 2021-06-20 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0007_alter_profile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]