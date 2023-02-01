from django.contrib import admin
from django.shortcuts import render, get_object_or_404

# Register your models here.

from shop.models import Category, Game


class GameInline(admin.TabularInline):
    model = Game


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('title',
                    'view_game_link',
                    'show_average_cost')
    inlines = [
        GameInline,
                ]

    @admin.display(description='games')
    def view_game_link(self, obj):
        from django.utils.html import format_html
        from django.urls import reverse
        from django.utils.http import urlencode

        count = obj.game_set.count()
        url = (
            reverse('admin:shop_game_changelist')
            + '?'
            + urlencode({'category_id': f'{obj.id}'})
        )
        return format_html('<a href="{}">{} Games</a>', url, count)

    @admin.display(description='average games cost')
    def show_average_cost(self, obj):
        """Функция для поиска средней стоимости игр в категории"""
        games_from_category = obj.game_set.all()
        average_price = 0
        if games_from_category:
            average_price = sum(list(map(lambda game: float(game.price), games_from_category))) / len(
                games_from_category)
        return f"{average_price:.2f} $"


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    date_hierarchy = 'release_date'
    list_display = (
        'name',
        'release_date',
        'show_pretty_price',
        'img_preview',
        'get_link'
        )
    list_editable = ('release_date',)
    list_filter = ('category',)
    search_fields = ('category__title', 'name')
    readonly_fields = ('img_tag',)
    actions = ("make_inactive",)

    @admin.display(description='custom price')
    def show_pretty_price(self, obj):
        return f"{obj.price} $"

    @admin.display(description='game image')
    def img_preview(self, obj):
        from django.utils.html import mark_safe
        return mark_safe(f'<img src = "{obj.game_image.url}" width = "150px" height="180px"/>')

    @admin.display(description='image tag')
    def img_tag(self, obj):
        from django.utils.html import mark_safe
        return mark_safe(f'<img src = "{obj.game_image.url}" width = "70px" height="90px"/>')

    @admin.display(description='game link')
    def get_link(self, obj):
        from django.utils.html import mark_safe
        return mark_safe(f'<a href="https://ru.wikipedia.org/wiki/{obj.name}">Search</a>')

    @admin.action(description='Перевести в неактивное состояние')
    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
