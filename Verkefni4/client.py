import socket, urllib.request

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        print("Sentu URL")
        a = input(">> ")
        # a = "http://data.pr4e.org/romeo.txt"

        s.sendall(a.encode())

        while True:
            i = s.recv(20000).decode()

            print(i)

            if i == "None" or i == "Url Doesn't Exist!":
                break



        # fhand = urllib.request.urlopen("https://mbl.is/")
        #print(fhand)

        # print(s.recv(1024).decode())
