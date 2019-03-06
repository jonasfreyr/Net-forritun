import socket
import urllib.request


HOST = '127.0.0.1'   # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(2)
    print("Server Started")

    conn, addr = s.accept()
    while True:
        url = conn.recv(1024).decode()

        try:
            fhand = urllib.request.urlopen("https://"+url+"/")

            characters = 0
            for line in fhand:
                words = line.decode()          #\n is considered a character
                                                #amend to line.decode().rstrip() if need
                characters = characters + len(words)
                if characters < 3000:
                    conn.sendall(line.decode().strip().encode())
            conn.sendall(str(characters).encode())
            conn.sendall(b"None")
        except:
            conn.sendall(b"Url Doesn't Exist!")

        # conn.sendall(str(tel).encode())
