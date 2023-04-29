from booking.models import DateRoute, Direction, TimeTrip
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (DateRouteSerializer, DirectionSerializer,
                          TimeTripSerializer)


class GetDirectionInfoView(APIView):
    """Класс для отображения всех активных направлений поездок в данном сервисе"""

    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]

    def get(self, request: Request) -> Response:
        """Получили сериализованные данные имеющихся направлений"""

        queryset = Direction.objects.filter(is_active=True).all()
        serializer_for_queryset = DirectionSerializer(instance=queryset, many=True)
        return Response({"directions": serializer_for_queryset.data})


class GetDateRouteInfoView(APIView):
    """Класс для отображения всех активных дат поездок"""

    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]

    def get(self, request: Request) -> Response:
        """Получили сериализованные данные имеющихся дат поездок"""

        queryset = DateRoute.objects.filter(is_active=True).all()
        serializer_for_queryset = DateRouteSerializer(instance=queryset, many=True)
        return Response({"dateroutes": serializer_for_queryset.data})


class GetTimeTripInfoView(APIView):
    """Класс для отображения всех имеющихся поездок"""

    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]

    def get(self, request: Request) -> Response:
        """Получили сериализованные данные поездок"""

        queryset = TimeTrip.objects.all()
        serializer_for_queryset = TimeTripSerializer(instance=queryset, many=True)
        return Response({"timetrips": serializer_for_queryset.data})


class DirectionDateRouteView(generics.ListAPIView):
    """Класс для отображения всех поездок в определенную дату и время"""

    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    serializer_class = TimeTripSerializer

    def get_queryset(self) -> QuerySet:
        """Получили сериализованные данные поездок"""

        # Получили список всех активных дат по заданному направлению
        direction_slug = self.kwargs["direction_slug"]
        direction = get_object_or_404(Direction, slug=direction_slug)
        date_routes = direction.dateroute_set.filter(
            is_active=True
        ).all()  # dateroute в dateroute_set взяли из модели
        # Получили список всех поездок в выбранный день
        date_route = self.kwargs["date_route"]
        day = get_object_or_404(date_routes, date_route=date_route)
        # timetrip в timetrip_set взяли из модели
        trip_times = day.timetrip_set.filter(direction=direction).all()

        return trip_times
