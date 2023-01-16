from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse, QueryDict
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, TemplateView


def fun_index(request: HttpRequest):
    return render(request, 'my_cv/index.html', {})


def fun_skills(request: HttpRequest):
    return render(request, 'my_cv/skills.html', {})


def fun_edu(request: HttpRequest):
    return render(request, 'my_cv/edu.html', {})


@csrf_exempt
@require_http_methods(['POST'])
def fun_sign(request: HttpRequest):
    return request.POST.dict()
