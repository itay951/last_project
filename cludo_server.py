import socket
import select
import time
from Party import *
o_c_s = []
m_t_s = []
p_t_a = []
s_s = socket.socket()
s_s.bind(('0.0.0.0', 8006))
s_s.listen(5)


def send_messages(wlist):
    for massage in m_t_s:
        print(m_t_s)
        print(massage)
        (c_s, data) = massage
        data = data.split(",")
        for party in wlist:
            if party is c_s:
                if data[0] == "oppo":
                    got_in = False
                    for parti in o_c_s:
                        if type(parti) is not socket.socket:
                            if not parti.full():
                                if parti.size == int(data[1]):
                                    parti.add(c_s)
                                    o_c_s.remove(c_s)
                                    got_in = True
                                    parti.player_cards[parti.amount-1].append(parti.suspects[0])
                                    parti.suspects.pop(0)
                                    c_s.send(("cards," + ",".join(parti.player_cards[parti.amount-1])).encode())
                                    names = ""
                                    for i in range(len(parti.players)):
                                        names = names + "," + parti.player_cards[i][-1]
                                    for player in parti.players:
                                        player.send(("names" + names).encode())
                                    time.sleep(1)
                                    if parti.full():
                                        for i in range(len(parti.players)):
                                            if i == parti.turn:
                                                parti.players[i].send("start,yes".encode())
                                            else:
                                                parti.players[i].send("start,no".encode())
                    if not got_in:
                        parte = Party(int(data[1]))
                        parte.add(c_s)
                        o_c_s.append(parte)
                        o_c_s.remove(c_s)
                        parte.player_cards[0].append(parte.suspects[0])
                        parte.suspects.pop(0)
                        c_s.send(("cards," + ",".join(parte.player_cards[0])).encode())
                        names = "," + parte.player_cards[0][-1]
                        c_s.send(("names" + names).encode())
            elif type(party) == Party:
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
                                party.players[party.turn].send("your turn".encode())
                            else:
                                player.send("player " + str(party.turn + 1) + "'s turn")
        m_t_s.remove(massage)


def main():
    while True:
        rlist, wlist, xlist = select.select([s_s] + o_c_s, o_c_s, [])
        for cu_s in rlist:
            if cu_s is s_s:
                (new_socket, ad) = s_s.accept()
                o_c_s.append(new_socket)

            else:
                if type(cu_s) == socket.socket:
                    data = cu_s.recv(1024).decode()
                    if data:
                        m_t_s.append((cu_s, data))
                    else:
                        if len(o_c_s) != 0:
                            for player in o_c_s:
                                if cu_s == player:
                                    o_c_s.remove(player)
                else:
                    for c_s in cu_s.players:
                        data = c_s.recv(4096).decode()
                        if data:
                            print(data)
                            m_t_s.append((c_s, data))
                            print(m_t_s)
                        else:
                            if len(o_c_s) != 0:
                                for party in o_c_s:
                                    for player in party.players:
                                        if c_s is player:
                                            party.remove(player)
                                        else:
                                            player.send("p_g_o".encode())
        send_messages(wlist)


if __name__ == '__main__':
    main()
