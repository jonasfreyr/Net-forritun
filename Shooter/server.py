import socket, _thread, time
start_time = time.time()
HOST = '127.0.0.1'   # Standard loopback interface address (localhost)
PORT = 65432
conns = []
id = 1
MAPNUM = 1

players = {}

def console():
    while True:
        i = input(">> ")

        if i == "time":
            print(time.time() - start_time)


def new_client(conn, addr, id):
    print("Connection started with:", addr)
    conn.sendall(str(MAPNUM).encode())
    if len(conns) == 1:
        conn.sendall(b'True')

    else:
        conn.sendall(b'False')

    while True:
        try:
            data = conn.recv(262144).decode()
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

            del players[id]
            conns.remove(conn)
            data = str(id).encode()
            for a in conns:
                a.sendall(data)

            break

        if conn not in conns:
            print("Connection ended with:", addr)
            del players[id]
            break

        else:
            players[id] = data

            temp = dict(players)

            del temp[id]

            conn.sendall(str(temp).encode())


def start_main():
    try:
        import shooter

    except:
        print("Main ended")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(2)

    _thread.start_new_thread(start_main, ())
    _thread.start_new_thread(console, ())
    while True:
        conn, addr = s.accept()

        conns.append(conn)

        _thread.start_new_thread(new_client, (conn, addr, id))

        id += 1
