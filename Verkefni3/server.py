import socket
import random


HOST = '127.0.0.1'   # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

words = ["rabbabari", "lyklaborð", "vöruaðskilaðarhyrna", "á", "ostaslaufa", "skjávarpi", "miata"]
letters = []
tries = 5

def get_word():
    return random.choice(words)

def make_word(word):
    s = ""
    for a in word:
        if a in letters:
            s = s + " " + a + " "

        else:
            s = s + " _ "

    return s

def check_word(word):
    for a in word:
        if a not in letters:
            return False

    return True

def check_letter(d, word):
    if d not in word:
        return 1

    else:
        return 0

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(2)
    print("Server Started")

    word = get_word()
    conn, addr = s.accept()
    while True:
        if check_word(word):
             conn.sendall(("Winner!" + "," + word).encode())
             break

        if tries == 0:
            conn.sendall(("Loser!" + "," + word).encode())
            break

        conn.sendall((make_word(word)+","+str(tries)).encode())

        data = conn.recv(1024).decode("utf-8")

        l = data[0].lower()

        if l not in letters:
            tries = tries - check_letter(l, word)

            letters.append(l)
