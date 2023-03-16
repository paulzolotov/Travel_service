import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

    HOST, PORT = "localhost", 9998  # Серверные параметры
    sock.connect((HOST, PORT))
    while True:
        data = input("Type the message to send:")
        data_bytes = data.encode()  # Кодирование в бинарную строку
        sock.sendall(data_bytes)
        data_bytes = sock.recv(1024)
        print(data_bytes)
        data = data_bytes.decode()
        print("Received:", data)
