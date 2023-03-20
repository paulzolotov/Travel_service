import csv
import io
from datetime import datetime

from django.contrib import admin
from django.core import serializers
from django.http import FileResponse, HttpResponse
from django.urls import reverse
from django.utils.html import format_html, mark_safe
from django.utils.http import urlencode

from shop.models import Basket, Category, Comment, Game, Log

# Register your models here.


class GameInline(admin.TabularInline):
    """
    TabularInline - подкласс InlineModelAdmin, который дает в возможность добавлять связанные записи одновременно.
    В нашем случае, мы получаем информацию о категории и о конкретных ее играх, заходя на страницу детализации
    категории.
    Интерфейс администратора имеет возможность редактировать модели на той же странице, что и родительская модель.
    """

    model = Game


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Класс для отображения на панели администратора информации о конкретной Категории."""

    list_display = ("title", "view_game_link", "show_average_cost")
    inlines = [
        GameInline,
    ]

    @admin.display(description="games")
    def view_game_link(self, obj):
        """Функция для подсчета количества игры в данной категории, а также генерации ссылки на эти игры"""
        count = obj.game_set.count()
        url = (
            reverse("admin:shop_game_changelist")
            + "?"
            + urlencode({"category_id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Games</a>', url, count)

    @admin.display(description="average games cost")
    def show_average_cost(self, obj):
        """Функция для поиска средней стоимости игр в категории"""
        games_from_category = obj.game_set.all()
        average_price = 0
        if games_from_category:
            average_price = sum(
                list(map(lambda game: float(game.price), games_from_category))
            ) / len(games_from_category)
        return f"{average_price:.2f} $"


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    """Класс для отображения на панели администратора информации о конкретной Игре."""

    date_hierarchy = "release_date"
    list_display = (
        "name",
        "release_date",
        "show_pretty_price",
        "img_preview",
        "get_link",
    )
    list_editable = ("release_date",)
    list_filter = ("category",)
    search_fields = ("category__title", "name")
    readonly_fields = ("img_tag",)
    actions = (
        "make_inactive",
        "export_as_json_csv",
        "export_to_csv",
    )

    @admin.display(description="custom price")
    def show_pretty_price(self, obj):
        """Функция для отображения кастомной записи для 'цены игры' (В данном случае добавили знак $)"""
        return f"{obj.price} $"

    @admin.display(description="game image")
    def img_preview(self, obj):
        """Функция для отображения иконки с игрой определенного размера"""
        return mark_safe(
            f'<img src = "{obj.game_image.url}" width = "150px" height="180px"/>'
        )

    @admin.display(description="image tag")
    def img_tag(self, obj):
        """Функция для отображения иконки с игрой определенного размера"""
        return mark_safe(
            f'<img src = "{obj.game_image.url}" width = "70px" height="90px"/>'
        )

    @admin.display(description="game link")
    def get_link(self, obj):
        """Функция для добавления ссылки на ресурс выбранной игры"""
        return mark_safe(
            f'<a href="https://ru.wikipedia.org/wiki/{obj.name}">Search</a>'
        )

    @admin.action(description="Switch to inactive state")
    def make_inactive(self, request, queryset):
        """Функция для перевода выбранных игр в строке 'action' в состояние 'inactive'"""
        queryset.update(is_active=False)

    @admin.action(description="Export to JSON-CSV")
    def export_as_json_csv(self, request, queryset):
        """Функция для выгрузки данных в виде логов в формате JSON-CSV"""
        response = FileResponse(
            io.BytesIO(serializers.serialize("json", queryset).encode("utf-8")),
            as_attachment=True,
            filename=f"log-{datetime.now()}.csv",
        )
        return response

    @admin.action(description="Export to CSV")
    def export_to_csv(self, request, queryset):
        """Функция для выгрузки данных в виде логов в формате CSV"""
        opts = self.model._meta
        # Создаем экземпляр HttpResponse, включающий кастомный text/csv-тип контента, чтобы сообщить браузеру,
        # что ответ должен обрабатываться как файл CSV. Также добавляется заголовок Content-Disposition, указывающий,
        # что HTTP-ответ содержит вложенный файл.
        response = HttpResponse(content_type="text/csv")
        response[
            "Content-Disposition"
        ] = f"attachment; filename={opts.verbose_name_plural}.csv"
        writer = csv.writer(response)
        # Записываем строку заголовка, включая имена полей.
        fields = opts.get_fields()  # Возвращает кортеж полей
        writer.writerow([field.verbose_name for field in fields])
        # Записываем строку для каждого объекта
        for obj in queryset:
            data_row = [getattr(obj, field.name) for field in fields]
            writer.writerow(data_row)
        return response


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    """Класс для отображения на панели администратора информации о Комментариях."""

    list_display = ("text", "pub_date", "rating", "game", "author")


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    """Класс для отображения на панели администратора информации о Логах."""

    list_display = ("log_datetime", "log_path", "log_user")
    readonly_fields = (
        "log_datetime",
        "log_path",
        "log_user",
    )  # Делаем так, чтобы логи нельзя было редактировать.
    search_fields = ("log_user",)


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    """Класс для отображения на панели администратора информации о Корзине пользователя."""

    list_display = ("user", "game", "created_datetime")
