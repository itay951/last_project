import socket
import select
import time
from Party import *
o_c_s = []
m_t_s = []
parties = []
s_s = socket.socket()
s_s.bind(('0.0.0.0', 8006))
s_s.listen(5)


def send_messages(wlist):
    for massage in m_t_s:
        (c_s, data) = massage
        data = data.split(",")
        for client in wlist:
            if client is c_s:
                if data[0] == "oppo":
                    got_in = False
                    for party in parties:
                        if not party.full():
                            if party.size == int(data[1]):
                                party.add(c_s)
                                got_in = True
                                party.player_cards[party.amount-1].append(party.suspects[0])
                                party.suspects.pop(0)
                                c_s.send(("cards," + ",".join(party.player_cards[party.amount-1])).encode())
                                names = ""
                                for i in range(len(party.players)):
                                    names = names + "," + party.player_cards[i][-1]
                                for player in party.players:
                                    player.send(("names" + names).encode())
                                time.sleep(1)
                                if party.full():
                                    for i in range(len(party.players)):
                                        if i == party.turn:
                                            party.players[i].send("start,yes".encode())
                                        else:
                                            party.players[i].send("start,no".encode())
                    if not got_in:
                        parte = Party(int(data[1]))
                        parte.add(c_s)
                        parties.append(parte)
                        parte.player_cards[0].append(parte.suspects[0])
                        parte.suspects.pop(0)
                        c_s.send(("cards," + ",".join(parte.player_cards[0])).encode())
                        names = "," + parte.player_cards[0][-1]
                        c_s.send(("names" + names).encode())
        for party in parties:
            if c_s in party.players:
                if data[0] == "update":
                    data = ",".join(data)
                    for player in party.players:
                        if player != "out":
                            if player is not c_s:
                                player.send(data.encode())
                if data[0] == "ask":
                    for i in range(len(party.player_cards)):
                        if party.players[i] is not c_s:
                            if data[1] in party.player_cards[i] or data[2] in party.player_cards[i] or data[3] in party.player_cards[i]:
                                if party.players[i] != "out":
                                    data = ",".join(data)
                                    party.players[i].send(data.encode())
                                    data = party.players[i].recv(1024)  # if something doesnt work in ask check here
                                    c_s.send(data)
                                else:
                                    if data[1] in party.player_cards[i]:
                                        c_s.send(data[1].encode())
                                    elif data[2] in party.player_cards[i]:
                                        c_s.send(data[2].encode())
                                    elif data[3] in party.player_cards[i]:
                                        c_s.send(data[3].encode())
                if data[0] == "accuse":
                    if data[1] in party.killer and data[2] in party.killer and data[3] in party.killer:
                        for player in party.players:
                            if c_s is player:
                                c_s.send("you won".encode())
                            else:
                                data = ",".join(data)
                                player.send((party.player_cards[party.turn+1][-1] + " won," + data).encode())
                    else:
                        for player in party.players:
                            if c_s is player:
                                c_s.send("you lost".encode())
                            else:
                                player.send((party.player_cards[party.turn+1][-1] + "accused and was wrong").encode())
                        party.remove(c_s)
                if data[0] == "end":
                    party.next_turn()
                    for player in party.players:
                        if player is party.players[party.turn]:
                            party.players[party.turn].send("turn".encode())

        m_t_s.remove(massage)


def main():
    while True:
        rlist, wlist, xlist = select.select([s_s] + o_c_s, o_c_s, [])
        for cu_s in rlist:
            if cu_s is s_s:
                (new_socket, ad) = s_s.accept()
                o_c_s.append(new_socket)
            else:
                data = cu_s.recv(1024).decode()
                if data:
                    m_t_s.append((cu_s, data))
                else:
                    print(data)
                    if len(o_c_s) != 0:
                        for player in o_c_s:
                            if cu_s == player:
                                o_c_s.remove(player)
                        for party in parties:
                            for player in party.players:
                                if cu_s == player:
                                    party.remove(player)
                send_messages(wlist)


if __name__ == '__main__':
    main()
