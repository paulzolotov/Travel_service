from django.contrib import admin

from articles.models import Users, Category, Posts


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_title',)


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'data_created', 'post_category_id')
