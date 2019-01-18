import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))


    while True:
        text = input("Choose a file ")

        s.sendall(text.encode())
        data = s.recv(1024)

        if data.decode() == "file found":
            while True:
                print("1. Read")
                print("2. Write")
                print("3. Erease contents")
                print("4. Exit")
                d = input(">> ")


                s.sendall(d.encode())
                data = s.recv(566000)

                if d == "1":
                    print(data.decode())

                elif d == "2":
                    print(data.decode())

                    i = input("Write to file ")
                    s.sendall(i.encode())

                    data = s.recv(1024)

                    if data.decode() == "Failed to write to file":
                        print(data.decode())
                        break

                    b = input("Do you want a newline? ")

                    if b == "yes":
                        s.sendall(b"yes")
                    else:
                        s.sendall(b"no")


                elif d == "3":
                    print(data.decode())

                elif d == "4":
                    break

