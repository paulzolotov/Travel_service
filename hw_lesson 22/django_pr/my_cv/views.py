from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .core.views_func import send_email


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def fun_index(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'my_cv/index.html', {})
    elif request.method == 'POST':
        #  Функция для отправки сообщения по email
        message = request.POST.get('message')
        out_mess = send_email(message)
        return HttpResponse(out_mess)


def fun_skills(request: HttpRequest):
    return render(request, 'my_cv/skills.html', {})


def fun_edu(request: HttpRequest):
    return render(request, 'my_cv/edu.html', {})
