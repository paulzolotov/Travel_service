from django.contrib import admin
from django.utils.html import format_html, mark_safe
from django.urls import reverse
from django.utils.http import urlencode
from django.core import serializers
from django.http import FileResponse, HttpResponse
from datetime import datetime
import io
import csv

# Register your models here.

from shop.models import Category, Game, Comment


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
    actions = ("make_inactive", 'export_as_json_csv', 'export_to_csv',)

    @admin.display(description='custom price')
    def show_pretty_price(self, obj):
        return f"{obj.price} $"

    @admin.display(description='game image')
    def img_preview(self, obj):
        return mark_safe(f'<img src = "{obj.game_image.url}" width = "150px" height="180px"/>')

    @admin.display(description='image tag')
    def img_tag(self, obj):
        return mark_safe(f'<img src = "{obj.game_image.url}" width = "70px" height="90px"/>')

    @admin.display(description='game link')
    def get_link(self, obj):
        return mark_safe(f'<a href="https://ru.wikipedia.org/wiki/{obj.name}">Search</a>')

    @admin.action(description='Switch to inactive state')
    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)

    @admin.action(description="Export to JSON-CSV")
    def export_as_json_csv(self, request, queryset):
        response = FileResponse(
            io.BytesIO(serializers.serialize("json", queryset).encode("utf-8")),
            as_attachment=True,
            filename=f"log-{datetime.now()}.csv", )
        return response

    @admin.action(description="Export to CSV")
    def export_to_csv(self, request, queryset):
        opts = self.model._meta
        # Создаем экземпляр HttpResponse, включающий кастомный text/csv-тип контента, чтобы сообщить браузеру,
        # что ответ должен обрабатываться как файл CSV. Также добавляется заголовок Content-Disposition, указывающий,
        # что HTTP-ответ содержит вложенный файл.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={opts.verbose_name_plural}.csv'
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
    list_display = ('text',
                    'pub_date',
                    'rating',
                    'game',
                    'author')
