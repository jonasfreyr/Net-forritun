import socket, os

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(2)
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            texts = []
            while True:
                data = conn.recv(1024)


                for file in os.listdir("./"):
                    if file.endswith(".txt"):
                         texts.append(file)

                if data.decode() in texts:
                    for file in texts:
                        if file == data.decode():
                            conn.sendall(b"file found")
                            while True:
                                data = conn.recv(1024)
                                if data.decode() == "1":
                                    with open(file, "r") as f:
                                        string = f.read()

                                    if string == "":
                                        string = "File is empty"
                                    conn.sendall(string.encode())

                                elif data.decode() == "2":
                                    conn.sendall(b"Ready to be written to")

                                    data = conn.recv(1024)
                                    try:
                                        with open(file, "a") as f:
                                            f.write(data.decode())

                                            conn.sendall(b"Succsesfully written to file")
                                    except:
                                        conn.sendall(b"Failed to write to file")
                                        break

                                    data = conn.recv(1024)
                                    if data.decode() == "yes":
                                        with open(file, "a") as f:
                                            f.write("\n")

                                elif data.decode() == "3":
                                     with open(file, "w") as f:
                                        f.write("")

                                        conn.sendall(b"Succsesfully ereased")

                                elif data.decode() == "4":
                                    conn.sendall(b"Succsesfully borked")
                                    break



                else:
                    conn.sendall(b"file not found")
except:
    print("No client")

