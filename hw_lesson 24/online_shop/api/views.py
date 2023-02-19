from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer

from shop.models import Game
from .serializers import GameSerializer


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
