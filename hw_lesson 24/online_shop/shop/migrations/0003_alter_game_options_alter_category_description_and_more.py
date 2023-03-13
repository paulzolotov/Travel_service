# Generated by Django 4.1.5 on 2023-01-19 07:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0002_game"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="game",
            options={"verbose_name": "Game", "verbose_name_plural": "Games"},
        ),
        migrations.AlterField(
            model_name="category",
            name="description",
            field=models.TextField(max_length=500, verbose_name="Category Description"),
        ),
        migrations.AlterField(
            model_name="game",
            name="description",
            field=models.TextField(max_length=500, verbose_name="Game Description"),
        ),
    ]
