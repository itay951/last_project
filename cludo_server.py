import socket
import select
import time
from Party import *
import sqlite3
o_c_s = []
m_t_s = []
parties = []
s_s = socket.socket()
s_s.bind(('0.0.0.0', 8006))
s_s.listen(5)
conn = sqlite3.connect("clue.db")


def end(party):
    # it gives the turn to the next player
    party.next_turn()
    while True:
        if party.players[party.turn] != "out":
            party.players[party.turn].send("turn,your".encode())
            break
        else:
            party.next_turn()
    for player2 in party.players:
        if player2 != "out":
            if player2 is not party.players[party.turn]:
                player2.send(("turn," + party.charecters[party.turn]).encode())


def answer(data, party):
    # sends the player's answer to the player that asked
    data = ",".join(data)
    party.players[party.turn].send(data.encode())


def accuse(c_s, data, party):
    # checks if the accusation was right or not
    if data[1] in party.killer and data[2] in party.killer and data[3] in party.killer:
        data.pop(0)
        data = ",".join(data)
        for player in party.players:
            if c_s is player:
                c_s.send(("game over,yes," + data).encode())
                o_c_s.remove(player)
            else:
                if player != "out":
                    player.send(("game over," + party.charecters[party.turn] + "," + data).encode())
                    o_c_s.remove(player)
        parties.remove(party)
    else:
        for player in party.players:
            if c_s is player:
                data[0] = "end"
                party.remove_player(player)
                o_c_s.remove(player)
                c_s.send("game over,no".encode())
        if party.all_out():
            for player in party.players:
                if player != "out":
                    player.send("all out".encode())
            parties.remove(party)
            return


def ask(c_s, data, party):
    # finds a player with the cards that are asked about
    for i in range(1, party.size + 1):
        if i + party.turn >= party.size:
            i -= party.size
        if party.players[party.turn + i] is not c_s:
            if data[1] in party.player_cards[party.turn + i] or data[2] in party.player_cards[party.turn + i] or data[3] in party.player_cards[party.turn + i]:
                if party.players[party.turn + i] != "out":
                    data = ",".join(data)
                    party.players[party.turn + i].send(data.encode())
                    break
                else:
                    if data[1] in party.player_cards[party.turn + i]:
                        c_s.send(("answer," + data[1]).encode())
                        break
                    elif data[2] in party.player_cards[party.turn + i]:
                        c_s.send(("answer," + data[2]).encode())
                        break
                    elif data[3] in party.player_cards[party.turn + i]:
                        c_s.send(("answer," + data[3]).encode())
                        break
        else:
            c_s.send("answer,no".encode())
            break


def update(c_s, data, party):
    # sends to all the players an update every turn
    data = ",".join(data)
    for player in party.players:
        if player != "out":
            if player is not c_s:
                player.send(data.encode())


def opponent(c_s, data):
    # receives the player's choice of the amount of players that will be in th game and finds a game with that amount of players
    got_in = False
    for party in parties:
        if not party.full():
            if party.size == int(data[1]):
                party.add(c_s)
                got_in = True
                party.player_cards[party.amount - 1].append(party.suspects[0])
                party.charecters.append(party.suspects[0])
                party.suspects.pop(0)
                c_s.send(("cards," + ",".join(party.player_cards[party.amount - 1])).encode())
                party.player_cards[party.amount - 1].pop(-1)
                names = ""
                for i in range(len(party.players)):
                    names = names + "," + party.charecters[i]
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
        parte.charecters.append(parte.suspects[0])
        parte.suspects.pop(0)
        c_s.send(("cards," + ",".join(parte.player_cards[0])).encode())
        parte.player_cards[parte.amount - 1].pop(-1)
        names = "," + parte.charecters[0]
        c_s.send(("names" + names).encode())


def register(c_s, data):
    wrong = False
    co = conn.cursor()
    for player in co.execute("SELECT * FROM table1"):
        if player[0] == data[1]:
            wrong = True
            break
    if wrong:
        c_s.send("register,bad".encode())
    else:
        co.execute("INSERT INTO table1 VALUES ('" + data[1] + "', '" + data[2] + "', '" + data[3] + "')")
        conn.commit()
        c_s.send(("register,good," + data[1]).encode())


def login(c_s, data):
    c = conn.cursor()
    for player in c.execute("SELECT * FROM table1"):
        if player[0] == data[1] and player[1] == data[2]:
            c_s.send(("login,good," + data[1]).encode())
            return
    c_s.send("login,bad".encode())


def end(party):
    # it gives the turn to the next player
    party.next_turn()
    while True:
        if party.players[party.turn] != "out":
            party.players[party.turn].send("turn,your".encode())
            break
        else:
            party.next_turn()
    for player2 in party.players:
        if player2 != "out":
            if player2 is not party.players[party.turn]:
                player2.send(("turn," + party.charecters[party.turn]).encode())


def answer(data, party):
    # sends the player's answer to the player that asked
    data = ",".join(data)
    party.players[party.turn].send(data.encode())


def accuse(c_s, data, party):
    # checks if the accusation was right or not
    if data[1] in party.killer and data[2] in party.killer and data[3] in party.killer:
        data.pop(0)
        data = ",".join(data)
        for player in party.players:
            if c_s is player:
                c_s.send(("game over,yes," + data).encode())
                o_c_s.remove(player)
            else:
                if player != "out":
                    player.send(("game over," + party.charecters[party.turn] + "," + data).encode())
                    o_c_s.remove(player)
        parties.remove(party)
    else:
        for player in party.players:
            if c_s is player:
                data[0] = "end"
                party.remove_player(player)
                o_c_s.remove(player)
                c_s.send("game over,no".encode())
        if party.all_out():
            for player in party.players:
                if player != "out":
                    player.send("all out".encode())
            parties.remove(party)
            return


def ask(c_s, data, party):
    # finds a player with the cards that are asked about
    for i in range(1, party.size + 1):
        if i + party.turn >= party.size:
            i -= party.size
        if party.players[party.turn + i] is not c_s:
            if data[1] in party.player_cards[party.turn + i] or data[2] in party.player_cards[party.turn + i] or data[3] in party.player_cards[party.turn + i]:
                if party.players[party.turn + i] != "out":
                    data = ",".join(data)
                    party.players[party.turn + i].send(data.encode())
                    break
                else:
                    if data[1] in party.player_cards[party.turn + i]:
                        c_s.send(("answer," + data[1]).encode())
                        break
                    elif data[2] in party.player_cards[party.turn + i]:
                        c_s.send(("answer," + data[2]).encode())
                        break
                    elif data[3] in party.player_cards[party.turn + i]:
                        c_s.send(("answer," + data[3]).encode())
                        break
        else:
            c_s.send("answer,no".encode())
            break


def update(c_s, data, party):
    # sends to all the players an update every turn
    data = ",".join(data)
    for player in party.players:
        if player != "out":
            if player is not c_s:
                player.send(data.encode())


def opponent(c_s, data):
    # receives the player's choice of the amount of players that will be in th game and finds a game with that amount of players
    got_in = False
    for party in parties:
        if not party.full():
            if party.size == int(data[1]):
                party.add(c_s)
                got_in = True
                party.player_cards[party.amount - 1].append(party.suspects[0])
                party.charecters.append(party.suspects[0])
                party.suspects.pop(0)
                c_s.send(("cards," + ",".join(party.player_cards[party.amount - 1])).encode())
                party.player_cards[party.amount - 1].pop(-1)
                names = ""
                for i in range(len(party.players)):
                    names = names + "," + party.charecters[i]
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
        parte.charecters.append(parte.suspects[0])
        parte.suspects.pop(0)
        c_s.send(("cards," + ",".join(parte.player_cards[0])).encode())
        parte.player_cards[parte.amount - 1].pop(-1)
        names = "," + parte.charecters[0]
        c_s.send(("names" + names).encode())


def send_messages(wlist):
    # organize the massages and calls the right function
    for massage in m_t_s:
        (c_s, data) = massage
        data = data.split(",")
        for client in wlist:
            if client is c_s:
                if data[0] == "register":
                    register(c_s, data)
                if data[0] == "login":
                    login(c_s, data)
                if data[0] == "oppo":
                    opponent(c_s, data)
        for party in parties:
            if c_s in party.players:
                if data[0] == "update":
                    update(c_s, data, party)
                if data[0] == "ask":
                    ask(c_s, data, party)
                if data[0] == "accuse":
                    accuse(c_s, data, party)
                if data[0] == "answer":
                    answer(data, party)
                if data[0] == "end":
                    end(party)
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
                    for player in o_c_s:
                        if cu_s == player:
                            o_c_s.remove(player)
                    for party in parties:
                        for player in party.players:
                            if cu_s == player:
                                party.remove_player(player)
                        if party.all_out():
                            for player in party.players:
                                if player != "out":
                                    player.send("all out".encode())
                            parties.remove(party)
                send_messages(wlist)


if __name__ == '__main__':
    main()
    conn.close()
