from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from .models import Direction, DateRoute, TimeTrip, Trip

# Create your views here.


def index(request: HttpRequest):
    """Функция предназначена для перехода к странице со списком направлений"""
    directions = Direction.objects.all()
    return render(request, "booking/index.html", context={"directions": directions})
