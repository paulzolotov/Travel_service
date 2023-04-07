# Generated by Django 4.1.7 on 2023-04-07 12:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0018_rename_data_route_dateroute_date_route'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direction',
            name='travel_time',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Travel time in minutes'),
        ),
        migrations.AlterField(
            model_name='timetrip',
            name='number_of_seats',
            field=models.IntegerField(default=20, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Number of seats'),
        ),
        migrations.AlterField(
            model_name='timetrip',
            name='price',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Price per seats'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='number_of_reserved_places',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Reserved places'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='user_comment',
            field=models.CharField(default='nothing', max_length=200, null=True, verbose_name='User Comment'),
        ),
    ]
