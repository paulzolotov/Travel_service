from rest_framework import serializers
from shop.models import Category, Game


class GameSerializer(serializers.Serializer):
    game_name = serializers.CharField(source='name', max_length=100)
    game_release_date = serializers.DateField(source='release_date')
    price = serializers.DecimalField(decimal_places=2, max_digits=5)
    description = serializers.CharField()
    category = serializers.CharField(source='category.title', max_length=100)
    slug = serializers.SlugField(max_length=50)

    def create(self, validated_data):  # создание модели
        return Game(**validated_data)

    def update(self, instance, validated_data):  # обновление модели
        instance.name = validated_data.get('game_name', instance.name)
        instance.release_date = validated_data.get('game_release_date', instance.release_date)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.category = validated_data.get('category', instance.category)
        instance.slug = validated_data.get('slug', instance.slug)
        return instance


class CategorySerializer(serializers.ModelSerializer):
    # ModelSerializer автоматически сгенерирует набор полей для вас, основываясь на модели.
    # Автоматически сгенерирует валидаторы для сериализатора, такие как unique_together валидаторы.
    # Включает в себя реализацию по умолчанию .create() и .update().
    class Meta:
        model = Category
        fields = ('id', 'title', 'slug', 'description', 'games_amount')
        # exclude = ('is_active',)  # Аналогично строке выше
