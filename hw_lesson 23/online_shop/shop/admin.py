from django.contrib import admin

# Register your models here.

from shop.models import Category, Game


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    ...
