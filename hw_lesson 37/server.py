import socket
import select

from Exceptions import *
from Operators import operators


def calculator(data):
    try:
        data = data.decode()
        a, operator, b = data.split()
    except ValueError as e:
        raise InputFormulaError('InputFormulaError')
    try:
        a, b = map(float, (a, b))
    except Exception as e:
        raise InputNumberError('InputNumberError')
    if operator not in operators:
        raise InputOperatorError('InputOperatorError')
    try:
        operation = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '**': lambda x, y: x ** y,
            '/': lambda x, y: x / y
        }
        return str(operation[operator](a, b))
    except ArithmeticError:
        raise CalculationError('CalculationError')


def handle(sock, addr):
    try:
        data = sock.recv(1024)
    except ConnectionError:
        print("Client suddenly closed while receiving")
        return False
    print(f"Received {data} from: {addr}")
    if not data:
        print("Disconnected by", addr)
        return False
    try:
        data_calc = calculator(data)
    except Exception as exp:
        print("Disconnected by", addr, exp)
        data_calc = f' , {exp}'
    print(f"Send: {data_calc} to: {addr}")
    try:
        data_calc = data_calc.encode()
    except ConnectionError:
        print(f"Client suddenly closed, cannot encode")
        return False
    try:
        sock.send(data_calc)
    except ConnectionError:
        print(f"Client suddenly closed, cannot send")
        return False
    return True


HOST, PORT = "", 9999
if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serv_sock:
        # AF_INET означает интернет сокет по протоколу IPv4,
        # SOCK_STREAM - транспортный протокол передачи информации информирующий о том, что будет исп-ся TCP
        serv_sock.bind((HOST, PORT))  # Привязка socket к адресу
        serv_sock.listen(1)  # Начинает слушать подключения
        inputs = [serv_sock]  # Доступные подключения
        outputs = []  # Подключения, которым мы будем передавать информацию
        while True:
            print("Waiting for connections or data...")
            # 3 входных объекта: # 1) Клиент, который готов работать с сервером.
            # 2) Клиент, который ожидает ответа от сервера. 3) Клиент, который возможно вызовет какие-то исключения.
            readable, writeable, exceptional = select.select(inputs, outputs, inputs)
            for sock in readable:
                if sock == serv_sock:
                    # Создание клиентского сокета, после каждого нового подключения.
                    # Возвращает адрес того кто обращается и сам объект подключения
                    sock, addr = serv_sock.accept()  # Should be ready.
                    print("Connected by", addr)
                    inputs.append(sock)
                else:  # Если сокет не серверный
                    addr = sock.getpeername()  # получение имени сокета
                    if not handle(sock, addr):  # Если произошло исключение какое-то, прервалась связь
                        # Disconnected
                        inputs.remove(sock)
                        if sock in outputs:
                            outputs.remove(sock)
                        sock.close()
