# Generated by Django 4.2 on 2023-05-03 13:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("booking", "0009_trip_user_trip_ticket"),
    ]

    operations = [
        migrations.CreateModel(
            name="Log",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "log_path",
                    models.CharField(max_length=300, verbose_name="request path"),
                ),
                (
                    "log_user",
                    models.CharField(max_length=100, verbose_name="request user"),
                ),
                (
                    "log_datetime",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Response datetime"
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="trip",
            name="user_trip_ticket",
            field=models.FileField(blank=True, null=True, upload_to="booking/"),
        ),
    ]
