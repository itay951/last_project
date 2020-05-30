import random
from Board import *
from pictures import *
from Sprite import *
import socket
import time
import tkinter as tk

while True:
    try:
        client_socket = socket.socket()
        client_socket.connect(("10.70.235.114", 8006))
        client_socket.settimeout(0)
        break
    except:
        pass
TURN = pictures.font.render("Miss Scarlett's turn", True, pictures.Black, pictures.White)
PLAYERS_OUT = False
BEGIN = False
PLAYED = False
LOOSE = False
GAME = True
loog = False
reg = False
board = Board()
pictures = pictures()
sprites = [Sprite("Miss Scarlett", 16, 0, pictures.red), Sprite("Colonel Mustard", 23, 7, pictures.yellow),
           Sprite("Rev. Green", 9, 24, pictures.green), Sprite("Professor Plum", 0, 5, pictures.purple),
           Sprite("Mrs. Peacock", 0, 18, pictures.blue), Sprite("Mrs. White", 14, 24, pictures.white),
           Sprite("dagger", 21, 1, pictures.dagger), Sprite("rope", 21, 10, pictures.rope),
           Sprite("candlestick", 1, 1, pictures.candlestick), Sprite("gun", 10, 1, pictures.gun),
           Sprite("pipe", 1, 7, pictures.pipe), Sprite("wrench", 1, 13, pictures.wrench)]
my_cards = []
my_character = None


def game_over(mass):
    # finish the game because some one accused and was right
    global GAME, LOOSE
    client_socket.send("end".encode())
    GAME = False
    if mass[1] == "yes":
        pictures.screen.fill(pictures.Black)
        massage = pictures.font2.render("you won", True, pictures.Black, pictures.White)
        pictures.screen.blit(massage, (100 * pictures.window_ratio, 50 * pictures.window_ratio))
        d_b = pictures.font2.render("Dr. Black was killed in the:", True, pictures.Black, pictures.White)
        pictures.screen.blit(d_b, (50 * pictures.window_ratio, 285 * pictures.window_ratio))
        for room in pictures.rooms_cards:
            if mass[2] == room[1]:
                pictures.screen.blit(room[0], (500 * pictures.window_ratio, 200 * pictures.window_ratio))
                pygame.display.flip()
        for character in pictures.characters_cards:
            if mass[3] == character[1]:
                mas = pictures.font2.render("by:", True, pictures.Black, pictures.White)
                pictures.screen.blit(mas, (650 * pictures.window_ratio, 285 * pictures.window_ratio))
                pictures.screen.blit(character[0], (700 * pictures.window_ratio, 200 * pictures.window_ratio))
                pygame.display.flip()
        for weapon in pictures.weapons_cards:
            if mass[4] == weapon[1]:
                mas = pictures.font2.render("with a:", True, pictures.Black, pictures.White)
                pictures.screen.blit(mas, (840 * pictures.window_ratio, 285 * pictures.window_ratio))
                pictures.screen.blit(weapon[0], (950 * pictures.window_ratio, 200 * pictures.window_ratio))
                pygame.display.flip()
    elif mass[1] == "no":
        pictures.screen.fill(pictures.Black)
        massage = pictures.font2.render("you lost", True, pictures.Black, pictures.White)
        pictures.screen.blit(massage, (100 * pictures.window_ratio, 50 * pictures.window_ratio))
        pygame.display.flip()
        return
    else:
        pictures.screen.fill(pictures.Black)
        massage = pictures.font2.render(mass[1] + " won", True, pictures.Black, pictures.White)
        pictures.screen.blit(massage, (100 * pictures.window_ratio, 50 * pictures.window_ratio))
        d_b = pictures.font2.render("Dr. Black was killed in the:", True, pictures.Black, pictures.White)
        pictures.screen.blit(d_b, (50 * pictures.window_ratio, 285 * pictures.window_ratio))
        for room in pictures.rooms_cards:
            if mass[2] == room[1]:
                pictures.screen.blit(room[0], (500 * pictures.window_ratio, 200 * pictures.window_ratio))
                pygame.display.flip()
        for character in pictures.characters_cards:
            if mass[3] == character[1]:
                mas = pictures.font2.render("by:", True, pictures.Black, pictures.White)
                pictures.screen.blit(mas, (650 * pictures.window_ratio, 285 * pictures.window_ratio))
                pictures.screen.blit(character[0], (700 * pictures.window_ratio, 200 * pictures.window_ratio))
                pygame.display.flip()
        for weapon in pictures.weapons_cards:
            if mass[4] == weapon[1]:
                mas = pictures.font2.render("with a:", True, pictures.Black, pictures.White)
                pictures.screen.blit(mas, (840 * pictures.window_ratio, 285 * pictures.window_ratio))
                pictures.screen.blit(weapon[0], (950 * pictures.window_ratio, 200 * pictures.window_ratio))
                pygame.display.flip()
        LOOSE = True
        return


def answer(mass):
    # receive an answer from another player and show it to you
    pictures.screen.fill(pictures.Black)
    if mass[1] == "no":
        anser = pictures.font2.render("no opponent has these cards", True, pictures.Black, pictures.White)
        pictures.screen.blit(anser, (450 * pictures.window_ratio, 50 * pictures.window_ratio))
        pygame.display.flip()
        time.sleep(2)
    else:
        for room in pictures.rooms_cards:
            if mass[1] == room[1]:
                pictures.screen.blit(room[0], (500 * pictures.window_ratio, 200 * pictures.window_ratio))
                pygame.display.flip()
                time.sleep(2)
        for character in pictures.characters_cards:
            if mass[1] == character[1]:
                pictures.screen.blit(character[0], (500 * pictures.window_ratio, 200 * pictures.window_ratio))
                pygame.display.flip()
                time.sleep(2)
        for weapon in pictures.weapons_cards:
            if mass[1] == weapon[1]:
                pictures.screen.blit(weapon[0], (500 * pictures.window_ratio, 200 * pictures.window_ratio))
                pygame.display.flip()
                time.sleep(2)
    client_socket.send("end".encode())


def ms_ask(mass):
    # checks which card you have from the question that was asked by another player and shows you which card you can choose to show
    mass.pop(0)
    pictures.screen.fill(pictures.Black)
    has_room = False
    has_sus = False
    has_wea = False
    for card in my_cards:
        if card.name == mass[0]:
            pictures.screen.blit(card.img, (200 * pictures.window_ratio, 100 * pictures.window_ratio))
            has_room = True
        if card.name == mass[1]:
            pictures.screen.blit(card.img, (350 * pictures.window_ratio, 100 * pictures.window_ratio))
            has_sus = True
        if card.name == mass[2]:
            pictures.screen.blit(card.img, (500 * pictures.window_ratio, 100 * pictures.window_ratio))
            has_wea = True
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if 100 * pictures.window_ratio < mouse_y < 275 * pictures.window_ratio:
                    if has_room:
                        if 200 * pictures.window_ratio < mouse_x < 320 * pictures.window_ratio:
                            client_socket.send(("answer," + mass[0]).encode())
                            return
                    if has_sus:
                        if 350 * pictures.window_ratio < mouse_x < 470 * pictures.window_ratio:
                            client_socket.send(("answer," + mass[1]).encode())
                            return
                    if has_wea:
                        if 500 * pictures.window_ratio < mouse_x < 620 * pictures.window_ratio:
                            client_socket.send(("answer," + mass[2]).encode())
                            return


def turn(mass):
    # print the players name who's turn it is and let you star your turn
    global PLAYED, TURN
    if mass[1] == "your":
        PLAYED = False
        torn = mass[1] + " turn"
        TURN = pictures.font.render(torn, True, pictures.Black, pictures.White)
    else:
        torn = mass[1] + "'s turn"
        TURN = pictures.font.render(torn, True, pictures.Black, pictures.White)


def ms_update(mass):
    # receive updates from other players and updates the placements of the game pieces
    global my_character, TURN, sprites
    for sprite in sprites:
        if mass[1] == sprite.name:
            board.grid[sprite.x][sprite.y].sprite = None
            sprite.x = int(mass[2])
            sprite.y = int(mass[3])
    update()
    draw(board, True, my_cards, TURN)


def names(mass):
    # prints and update the opponent list in the waiting room
    mass.pop(0)
    draw_waiting_room(mass, True)


def make_cards(massage):
    # receives a list of names of the cards that the player has and makes a list of images of the cards the player have
    for i in range(len(massage)):
        for room in pictures.rooms_cards:
            if massage[i] == room[1]:
                if i < 4:
                    my_cards.append(Sprite(massage[i], 670*pictures.window_ratio + 135*pictures.window_ratio * i, 35*pictures.window_ratio, room[0]))
                elif i == 4:
                    my_cards.append(Sprite(massage[i], 670*pictures.window_ratio, 210*pictures.window_ratio, room[0]))
                elif i == 5:
                    my_cards.append(Sprite(massage[i], 1075*pictures.window_ratio, 210*pictures.window_ratio, room[0]))
        for character in pictures.characters_cards:
            if massage[i] == character[1]:
                if i < 4:
                    my_cards.append(Sprite(massage[i], 670*pictures.window_ratio + 135*pictures.window_ratio * i, 35*pictures.window_ratio, character[0]))
                elif i == 4:
                    my_cards.append(Sprite(massage[i], 670*pictures.window_ratio, 210*pictures.window_ratio, character[0]))
                elif i == 5:
                    my_cards.append(Sprite(massage[i], 1075*pictures.window_ratio, 210*pictures.window_ratio, character[0]))
        for weapon in pictures.weapons_cards:
            if massage[i] == weapon[1]:
                if i < 4:
                    my_cards.append(Sprite(massage[i], 670*pictures.window_ratio + 135*pictures.window_ratio * i, 35*pictures.window_ratio, weapon[0]))
                elif i == 4:
                    my_cards.append(Sprite(massage[i], 670*pictures.window_ratio, 210*pictures.window_ratio, weapon[0]))
                elif i == 5:
                    my_cards.append(Sprite(massage[i], 1075*pictures.window_ratio, 210*pictures.window_ratio, weapon[0]))


def cards(mass):
    # receive the character's name to play with and the cards the player will have
    global my_character
    mass.pop(0)
    for k in range(6):
        if mass[-1] == sprites[k].name:
            my_character = sprites[k]
    mass.pop(-1)
    make_cards(mass)


def start(mass):
    # starts the game and lets the first player to start
    global TURN, BEGIN, PLAYED
    if mass[1] == "yes":
        TURN = pictures.font.render("your turn", True, pictures.Black, pictures.White)
        BEGIN = True
        PLAYED = False
    else:
        BEGIN = True
        PLAYED = True


def all_out():
    # ends the game because the rest of the players left
    global PLAYERS_OUT
    pictures.screen.fill(pictures.Black)
    left = pictures.font2.render("rest of the players got out", True, pictures.Black, pictures.White)
    pictures.screen.blit(left, (200 * pictures.window_ratio, 100 * pictures.window_ratio))
    pygame.display.flip()
    PLAYERS_OUT = True
    return


def ms_login(mass):
    global loog
    if mass[1] == "good":
        loog = True
    else:
        log_in(True)


def ms_register(mass):
    global reg
    if mass[1] == "good":
        reg = True
    else:
        register(True)


def get_message():
    # tries to get a message from the server and if it gets a message it checks what it says and call the right function
    try:
        mass = client_socket.recv(1024).decode()
    except:
        return
    mass = mass.split(",")
    if mass[0] == "register":
        ms_register(mass)
    if mass[0] == "login":
        ms_login(mass)
    if mass[0] == "all out":
        all_out()
        return
    if mass[0] == "start":
        start(mass)
        return
    elif mass[0] == "cards":
        cards(mass)
        return
    elif mass[0] == "names":
        names(mass)
        return
    elif mass[0] == "update":
        ms_update(mass)
        return
    elif mass[0] == "turn":
        turn(mass)
        return
    elif mass[0] == "ask":
        ms_ask(mass)
        return
    elif mass[0] == "answer":
        answer(mass)
        return
    elif mass[0] == "game over":
        game_over(mass)


def ask(room):
    # gets what the player wants to ask about and sends it to the server
    global client_socket
    sus, wea = draw_ask_lists()
    client_socket.send(("ask," + room + "," + sus + "," + wea).encode())
    get_message()


def accuse(room):
    # gets what the player wants to accuse at and sends it to the server
    global client_socket
    sus, wea = draw_ask_lists()
    client_socket.send(("accuse," + room + "," + sus + "," + wea).encode())
    get_message()


def update():
    # update the places of the players
    for sprite in sprites:
        board.grid[sprite.x][sprite.y].sprite = sprite.img


def move(deck):
    # generates two random numbers as the cubes and call the roll function
    rand = random.randint(1, 6)
    rand2 = random.randint(1, 6)
    draw_cube(rand, rand2)
    pygame.display.update()
    rand3 = rand + rand2
    returned = board.roll(my_character, rand3, deck, my_cards, TURN)
    update()
    if returned:
        return False
    return True


def login_page():
    global loog, reg
    first = True
    while first:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if 400 * pictures.window_ratio < mouse_y < 500 * pictures.window_ratio:
                    if 100 * pictures.window_ratio < mouse_x < 340 * pictures.window_ratio:
                        log_in()
                if 400 * pictures.window_ratio < mouse_y < 500 * pictures.window_ratio:
                    if 600 * pictures.window_ratio < mouse_x < 980 * pictures.window_ratio:
                        register()
        button = pictures.font3.render("login", True, pictures.Black, pictures.White)
        pictures.screen.blit(pictures.bg, (0, 0))
        pictures.screen.blit(button, (100 * pictures.window_ratio, 400 * pictures.window_ratio))
        button2 = pictures.font3.render("register", True, pictures.Black, pictures.White)
        pictures.screen.blit(button2, (600 * pictures.window_ratio, 400 * pictures.window_ratio))
        pygame.display.flip()
        get_message()
        if loog or reg:
            return True


def first_page():
    first = True
    while first:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if 400 * pictures.window_ratio < mouse_y < 500 * pictures.window_ratio:
                    if 100 * pictures.window_ratio < mouse_x < 620 * pictures.window_ratio:
                        first = False
        button = pictures.font3.render("start game", True, pictures.Black, pictures.White)
        pictures.screen.blit(pictures.bg, (0, 0))
        pictures.screen.blit(button, (100 * pictures.window_ratio, 400 * pictures.window_ratio))
        pygame.display.flip()
    draw_waiting_room()
    return True


def log(user, password, login):
    client_socket.send(("login," + user + "," + password).encode())
    login.destroy()


def log_in(tried=False):
    login = tk.Tk()
    name_label = tk.Label(text="user name")
    name_label.pack()
    name_entry = tk.Entry()
    name_entry.pack()
    password_label = tk.Label(text="password")
    password_label.pack()
    password_entry = tk.Entry(show="*")
    password_entry.pack()
    check = tk.Button(text="log in", command=lambda: log(name_entry.get(), password_entry.get(), login))
    check.pack()
    wrong = tk.Label(text="wrong password")
    if tried:
        wrong.pack()
    login.mainloop()


def regi(name, password, fname, regster):
    client_socket.send(("register," + name + "," + password + "," + fname).encode())
    regster.destroy()


def register(tried=False):
    regster = tk.Tk()
    f_name_label = tk.Label(text="first name")
    f_name_label.pack()
    f_name_entry = tk.Entry()
    f_name_entry.pack()
    name_label = tk.Label(text="user name")
    name_label.pack()
    name_entry = tk.Entry()
    name_entry.pack()
    password_label = tk.Label(text="password")
    password_label.pack()
    password_entry = tk.Entry(show="*")
    password_entry.pack()
    check = tk.Button(text="register", command=lambda: regi(name_entry.get(), password_entry.get(), f_name_entry.get(), regster))
    check.pack()
    wrong = tk.Label(text="this name is already used")
    if tried:
        wrong.pack()
    regster.mainloop()


def lobby_page():
    global PLAYERS_OUT
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if 100 * pictures.window_ratio < mouse_y < 200 * pictures.window_ratio:
                    if 450 * pictures.window_ratio < mouse_x < 500 * pictures.window_ratio:
                        client_socket.send(("oppo," + str(3)).encode())
                        return True
                    if 550 * pictures.window_ratio < mouse_x < 600 * pictures.window_ratio:
                        client_socket.send(("oppo," + str(4)).encode())
                        return True
                    if 650 * pictures.window_ratio < mouse_x < 700 * pictures.window_ratio:
                        client_socket.send(("oppo," + str(5)).encode())
                        return True
                    if 750 * pictures.window_ratio < mouse_x < 800 * pictures.window_ratio:
                        client_socket.send(("oppo," + str(6)).encode())
                        return True

                    if PLAYERS_OUT:
                        return False


def waiting_room():
    global PLAYERS_OUT, BEGIN
    while True:
        get_message()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False

        if PLAYERS_OUT:
            return False
        if BEGIN:
            return True


def game_page():
    global client_socket, TURN, my_cards, board, PLAYED, PLAYERS_OUT, LOOSE, sprites, my_character, GAME
    deck_up = False
    while True:
        if not GAME:
            return True
        update()
        draw(board, deck_up, my_cards, TURN)
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if not PLAYED:
                        client_socket.send("end".encode())
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if not PLAYED:
                            client_socket.send("end".encode())
                        return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if (pictures.lists_button_pos[0] + 75 * pictures.window_ratio >= mouse_x >= pictures.lists_button_pos[0]) and \
                            (pictures.lists_button_pos[1] + 35 * pictures.window_ratio >= mouse_y >= pictures.lists_button_pos[1]):
                        deck_up = False
                    if (pictures.cards_button_pos[0] <= mouse_x <= pictures.cards_button_pos[0] + 100 * window_ratio) and \
                            (pictures.cards_button_pos[1] <= mouse_y <= pictures.cards_button_pos[1] + 35 * window_ratio):
                        deck_up = True
                    draw(board, deck_up, my_cards, TURN)
                    if not deck_up:
                        for i in range(3):
                            for j in range(3):
                                if pictures.rooms[i][j].x <= mouse_x <= pictures.rooms[i][j].x + 80 * pictures.window_ratio and \
                                        pictures.rooms[i][j].y <= mouse_y <= pictures.rooms[i][j].y + 40 * pictures.window_ratio:
                                    if event.button == 1:
                                        pictures.rooms[i][j].img = pictures.check
                                    if event.button == 3:
                                        pictures.rooms[i][j].img = pictures.red_x
                                if i < 2:
                                    if pictures.weapons[i][j].x <= mouse_x <= pictures.weapons[i][j].x + 80 * pictures.window_ratio and \
                                            pictures.weapons[i][j].y <= mouse_y <= pictures.weapons[i][j].y + 40 * pictures.window_ratio:
                                        if event.button == 1:
                                            pictures.weapons[i][j].img = pictures.check
                                        if event.button == 3:
                                            pictures.weapons[i][j].img = pictures.red_x
                                    if pictures.suspects[i][j].x <= mouse_x <= pictures.suspects[i][j].x + 100 * pictures.window_ratio and \
                                            pictures.suspects[i][j].y <= mouse_y <= pictures.suspects[i][j].y + 40 * pictures.window_ratio:
                                        if event.button == 1:
                                            check = pygame.transform.scale(pictures.check, (int(100 * pictures.window_ratio), int(40 * pictures.window_ratio)))
                                            pictures.suspects[i][j].img = check
                                        if event.button == 3:
                                            red_x = pygame.transform.scale(pictures.red_x, (int(100 * pictures.window_ratio), int(40 * pictures.window_ratio)))
                                            pictures.suspects[i][j].img = red_x
                    if not PLAYED:
                        if event.button == 1:
                            if (pictures.roll_button_pos[0] <= mouse_x <= pictures.roll_button_pos[0] + 50 * pictures.window_ratio) and \
                                    (pictures.roll_button_pos[1] <= mouse_y <= pictures.roll_button_pos[1] + 35 * pictures.window_ratio):
                                gm = move(deck_up)
                                if not gm:
                                    client_socket.send("end, ".encode())
                                    return gm
                                PLAYED = True
                                for sprite in sprites:
                                    if sprite.name == my_character.name:
                                        sprite.x = my_character.x
                                        sprite.y = my_character.y
                                update()
                                draw(board, deck_up, my_cards, TURN)
                                client_socket.send(("update," + my_character.name + "," + str(my_character.x) + "," + str(my_character.y)).encode())
                                time.sleep(1)
                                client_socket.send("end, ".encode())
                                pictures.screen.fill(pictures.Black)
                            if (pictures.accuse_button_pos[0] + 200 * pictures.window_ratio >= mouse_x >= pictures.accuse_button_pos[0]) and \
                                    (pictures.accuse_button_pos[1] + 35 * window_ratio >= mouse_y >= pictures.accuse_button_pos[1]):
                                if board.grid[my_character.x][my_character.y].ident == "room":
                                    accuse(board.grid[my_character.x][my_character.y].room_name)
                                    if PLAYERS_OUT:
                                        pictures.screen.fill(pictures.Black)
                                        mas = pictures.font2.render("all other players left game", True, pictures.Black, pictures.White)
                                        pictures.screen.blit(mas, (450 * pictures.window_ratio, 50 * pictures.window_ratio))
                                        pygame.display.flip()
                                    else:
                                        PLAYED = True
                            if (pictures.question_button_pos[0] + 200 * window_ratio >= mouse_x >= pictures.question_button_pos[0]) and \
                                    (pictures.question_button_pos[1] + 35 * window_ratio >= mouse_y >= pictures.question_button_pos[1]):
                                if board.grid[my_character.x][my_character.y].ident == "room":
                                    ask(board.grid[my_character.x][my_character.y].room_name)
                                    if PLAYERS_OUT:
                                        pictures.screen.fill(pictures.Black)
                                        mas = pictures.font2.render("all other players left game", True, pictures.Black, pictures.White)
                                        pictures.screen.blit(mas, (450 * pictures.window_ratio, 50 * pictures.window_ratio))
                                        pygame.display.flip()
                                        return True
                                    else:
                                        PLAYED = True

            if PLAYED:
                get_message()
                if PLAYERS_OUT:
                    pictures.screen.fill(pictures.Black)
                    mas = pictures.font2.render("all other players left game", True, pictures.Black, pictures.White)
                    pictures.screen.blit(mas, (450 * pictures.window_ratio, 50 * pictures.window_ratio))
                    pygame.display.flip()
                    return True
                if LOOSE:
                    return True

        except:
            return False


def end_page():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


def main():
    move_on = login_page()
    if move_on:
        move_on = first_page()
    if move_on:
        move_on = lobby_page()

    if move_on:
        move_on = waiting_room()

    if move_on:
        move_on = game_page()
    client_socket.close()
    if move_on:
        end_page()


if __name__ == '__main__':
    main()
