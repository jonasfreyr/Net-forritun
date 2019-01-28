import socket, _thread

HOST = '0.0.0.0'   # Standard loopback interface address (localhost)
PORT = 65432
conns = []
id = 1
MAPNUM = 0

def new_client(conn, addr, id):
    print("Connection started with:", addr)
    conn.sendall(str(MAPNUM).encode())
    while True:
        try:
            data = conn.recv(65536).decode()
            try:
                data = eval(data)
            except:
                s = ""
                count = 0
                for a in data:
                    s = s + a

                    if a == "{":
                        count += 1

                    elif a == "}":
                        count -= 1

                    if count == 0:
                        break


                data = eval(s)

            data["id"] = id

            # print(data)

            data = str(data).encode()

        except:
            print("Connection ended with:", addr)

            conns.remove(conn)
            data = str(id).encode()
            for a in conns:
                a.sendall(data)

            break

        if conn not in conns:
            print("Connection ended with:", addr)
            break

        else:
            for a in conns:
                if a != conn:
                    a.sendall(data)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(2)
    while True:
        conn, addr = s.accept()

        conns.append(conn)

        _thread.start_new_thread(new_client, (conn, addr, id))

        id += 1