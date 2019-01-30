import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        data = s.recv(1024).decode("utf-8")

        data = data.split(",")

        if data[0] == "Winner!" or data[0] == "Loser!":
            print("Word:", data[1])
        else:
            print("Life:", data[1])
            
        print(data[0])

        if data[0] == "Winner!" or data[0] == "Loser!":
            break

        a = str(input(">> "))

        s.sendall(a.encode())
