import socket
from dotenv import dotenv_values


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

    socket_data = dotenv_values('./.env')['SOCKET_CLIENT']
    HOST = socket_data.split(':')[0]
    PORT = socket_data.split(':')[-1]
    # HOST, PORT = "localhost", 9999  # Серверные параметры
    sock.connect((HOST, int(PORT)))
    while True:
        data = input("Type the message to send:")
        data_bytes = data.encode()  # Кодирование в бинарную строку
        sock.sendall(data_bytes)
        data_bytes = sock.recv(1024)
        data = data_bytes.decode()
        print("Received:", data)
