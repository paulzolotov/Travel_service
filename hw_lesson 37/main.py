"""
Вынесите бизнес-логику (части кода, в которых происходит непосредственно определение какая команда передана,
какие числа и выполнение вычисления) в отдельный модуль.
Затем в новом модуле создайте aiohttp, который бы переиспользовал уже
существующую логику и так же мог повторять поведение сокет-сервера.
"""

from aiohttp import web
from numeric_processor import NumericOperationProcessor as nop


async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


async def variable_handler(request):
    expression = request.match_info.get('expression', "")
    print(expression)
    try:
        data_calc = nop.calculator(expression)
    except Exception as exp:
        data_calc = f' "", Error: {exp}'

    return web.Response(text=data_calc)


app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle),
                web.get('/calculate/{expression}', variable_handler)])

if __name__ == '__main__':
    web.run_app(app)
