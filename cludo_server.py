import random
from pictures import *
import socket
import threading
import time
from Party import *
s_s = socket.socket()
s_s.bind(('0.0.0.0', 23))
s_s.listen(5)


def send_messages():
    pass


def main():
    # killer info
    rand_weapon = random.randint(0, 5)
    rand_suspect = random.randint(0, 5)
    rand_room = random.randint(0, 8)
    killer = (pictures.rooms_names[rand_room], pictures.suspects_names[rand_suspect], pictures.weapons_names[rand_weapon])
    player_parties = [s_s]
    # socket
    while True:
        (new_socket, ad) = s_s.accept()
        new_socket.send("how much in a party?".encode())
        answer = new_socket.recv(1024).decode()
        answer.split(" ")
        if answer[0] == "new":
            player_party = Party(answer[1])
            player_party.add(new_socket)
            player_parties.append(player_party)
        else:
            for party in player_parties:
                if int(answer[0]) == party.size:
                    if party.size > party.amount:
                        party.add(new_socket)
                        break


if __name__ == '__main__':
    main()

