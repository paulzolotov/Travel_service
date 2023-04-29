from booking.models import DateRoute, Direction, TimeTrip
from rest_framework import serializers


class DirectionSerializer(serializers.ModelSerializer):
    """Класс, формирующий сериализованные данные модели Direction"""

    # ModelSerializer автоматически сгенерирует набор полей для вас, основываясь на модели.
    # Автоматически сгенерирует валидаторы для сериализатора, такие как unique_together валидаторы.
    # Включает в себя реализацию по умолчанию .create() и .update().
    class Meta:
        model = Direction
        fields = (
            "id",
            "name",
            "slug",
            "start_point",
            "end_point",
            "travel_time",
        )


class DateRouteSerializer(serializers.ModelSerializer):
    """Класс, формирующий сериализованные данные модели DateRoute"""

    class Meta:
        model = DateRoute
        fields = ("id", "date_route", "direction_name")


class TimeTripSerializer(serializers.ModelSerializer):
    """Класс, формирующий сериализованные данные модели TimeTrip"""

    class Meta:
        model = TimeTrip
        fields = (
            "id",
            "departure_time",
            "date_of_the_trip",
            "direction",
            "number_of_seats",
            "price",
            "number_of_free_places_in_trip",
            "number_of_reserved_places_in_trip",
        )
