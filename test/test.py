import socket
import _thread

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

def receive_data(conn, int):
    while True:
        data = conn.recv(1024).decode("utf-8")
        print(data)
        print('>> ', end="", flush=True)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    print('Sláðu inn Notenda nafn')
    a = input(">> ")
    a = a.encode()
    s.sendall(a)
    while True:
        _thread.start_new_thread(receive_data, (s, 2))
        a = input(">> ")
        a = a.encode()
        s.sendall(a)


