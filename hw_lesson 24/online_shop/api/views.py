from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework import generics
from rest_framework import filters as rest_filters

from shop.models import Game, Category
from .serializers import GameSerializer, CategorySerializer
import random
from django_filters import rest_framework as filters


# Create your views here.

class GetGameInfoView(APIView):

    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]

    def get(self, request):
        if self.random_request():
            many_flag = False
            queryset = Game.objects.all().order_by('?')[1]  # Получаю первую игру с упорядоченного в случайном
            # порядке списка игр через order_by('?')
        else:
            many_flag = True
            queryset = Game.objects.all()
        serializer_for_queryset = GameSerializer(instance=queryset, many=many_flag)
        return Response({"games": serializer_for_queryset.data})

     def random_request(self):
        query = self.request.query_params.get('random', None)
        return query and query.upper() == 'TRUE'


class GetCategoryInfoView(APIView):

    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]

    def get(self, request):
        queryset = Category.objects.filter(is_active=True).all()
        serializer_for_queryset = CategorySerializer(instance=queryset, many=True)
        return Response({"categories": serializer_for_queryset.data})


class GetCategoryGamesInfoView(generics.ListAPIView):

    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    serializer_class = GameSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Game.objects.filter(is_active=True).filter(category__title=category.title())


class GetGameInfoFilterView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['category__title', 'release_date']


class GetGameInfoSearchView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    filter_backends = [rest_filters.SearchFilter]
    search_fields = ['name']


class GetGameInfoOrderView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    filter_backends = [rest_filters.OrderingFilter]
    ordering_fields = ['name', 'release_date', 'price']
