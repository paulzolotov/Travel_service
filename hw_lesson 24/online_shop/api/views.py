from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework import generics

from shop.models import Game, Category
from .serializers import GameSerializer, CategorySerializer
import random


# Create your views here.

class GetGameInfoView(APIView):

    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]

    def get(self, request):
        if self.get_queryset() == 'true' or self.get_queryset() == 'True':
            all_games = Game.objects.all()
            random_game = random.randint(0, all_games.count()-1)
            queryset = all_games[random_game]
            serializer_for_queryset = GameSerializer(instance=queryset)
        else:
            queryset = Game.objects.all()
            serializer_for_queryset = GameSerializer(instance=queryset, many=True)
        return Response({"games": serializer_for_queryset.data})

    def get_queryset(self):
        return self.request.query_params.get('random', None)


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
