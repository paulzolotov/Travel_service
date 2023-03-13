# Generated by Django 4.1.5 on 2023-01-20 07:14

import django.db.models.deletion
from django.db import migrations, models

import shop.models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0007_alter_game_game_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="description",
            field=models.TextField(verbose_name="Category Description"),
        ),
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(verbose_name="Category Slug"),
        ),
        migrations.AlterField(
            model_name="category",
            name="title",
            field=models.CharField(max_length=100, verbose_name="Category Title"),
        ),
        migrations.AlterField(
            model_name="game",
            name="category",
            field=models.ForeignKey(
                default=shop.models.Category.get_default_category_pk,
                null=True,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to="shop.category",
                verbose_name="Game Category",
            ),
        ),
        migrations.AlterField(
            model_name="game",
            name="description",
            field=models.TextField(verbose_name="Game Description"),
        ),
        migrations.AlterField(
            model_name="game",
            name="name",
            field=models.CharField(max_length=10, verbose_name="Game Name"),
        ),
        migrations.AlterField(
            model_name="game",
            name="pub_date",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Game publication date"
            ),
        ),
        migrations.AlterField(
            model_name="game",
            name="slug",
            field=models.SlugField(verbose_name="Game Slug"),
        ),
    ]
