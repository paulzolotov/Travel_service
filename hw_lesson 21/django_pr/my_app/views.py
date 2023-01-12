from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse, QueryDict
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, TemplateView
from .core.views_func import factorial
import requests


def fun_index(request: HttpRequest):
    return HttpResponse('Hello from Django')


class MyClassBasedViewQuote(View):

    def get(self, request, *args, **kwargs):
        if kwargs.get('number'):
            number = kwargs['number']
        else:
            number = 1
        req_list = [requests.get('https://api.kanye.rest').json().get('quote') for _ in range(number)]
        return render(request, 'my_app/quotes.html', {'req_list': req_list})


# class MyClassBasedViewQuote(TemplateView):
#
#     template_name = 'my_app/quotes.html'
#
#     def get_context_data(self, **kwargs):
#         if kwargs.get('number'):
#             number = kwargs['number']
#         else:
#             number = 1
#         req_list = [requests.get('https://api.kanye.rest').json().get('quote') for _ in range(number)]
#         context = super().get_context_data(**kwargs)
#         context['req_list'] = req_list
#         return context


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def fun_factorial(request: HttpRequest):
    if request.method == 'GET':
        return HttpResponse('To find out the factorial of a number, send it in the body of the request.')
    elif request.method == 'POST':
        if not request.POST:
            return HttpResponse('The body of the request is empty. Please send some parameters.')
        else:
            number = int(request.POST.get('number'))
            fact = factorial(number)
            request.POST._mutable = True  # необходимо для добавления новой записи в QueryDict
            request.POST['factorial'] = fact
            return HttpResponse(request)
