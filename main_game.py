import random
from Board import *
from pictures import *
from Sprite import *
import socket
import time


board = Board()
pictures = pictures()
sprites = []
sprites.append(Sprite("Miss Scarlett", 16, 0, pictures.red))
sprites.append(Sprite("Colonel Mustard", 23, 7, pictures.yellow))
sprites.append(Sprite("Rev. Green", 9, 24, pictures.green))
sprites.append(Sprite("Professor Plum", 0, 5, pictures.purple))
sprites.append(Sprite("Mrs. Peacock", 0, 18, pictures.blue))
sprites.append(Sprite("Mrs. White", 14, 24, pictures.white))
sprites.append(Sprite("dagger", 21, 1, pictures.dagger))
sprites.append(Sprite("rope", 21, 10, pictures.rope))
sprites.append(Sprite("candlestick", 1, 1, pictures.candlestick))
sprites.append(Sprite("gun", 10, 1, pictures.gun))
sprites.append(Sprite("pipe", 1, 7, pictures.pipe))
sprites.append(Sprite("wrench", 1, 13, pictures.wrench))
my_cards = []
my_character = None


def make_cards(massage):
    for i in range(len(massage)):
        for room in pictures.rooms_cards:
            if massage[i] == room[1]:
                if i < 4:
                    my_cards.append(Sprite(massage[i], 670 + 135 * i, 35, room[0]))
                elif i == 4:
                    my_cards.append(Sprite(massage[i], 670, 210, room[0]))
                elif i == 5:
                    my_cards.append(Sprite(massage[i], 1075, 210, room[0]))
        for character in pictures.characters_cards:
            if massage[i] == character[1]:
                if i < 4:
                    my_cards.append(Sprite(massage[i], 670 + 135 * i, 35, character[0]))
                elif i == 4:
                    my_cards.append(Sprite(massage[i], 670, 210, character[0]))
                elif i == 5:
                    my_cards.append(Sprite(massage[i], 1075, 210, character[0]))
        for weapon in pictures.weapons_cards:
            if massage[i] == weapon[1]:
                if i < 4:
                    my_cards.append(Sprite(massage[i], 670 + 135 * i, 35, weapon[0]))
                elif i == 4:
                    my_cards.append(Sprite(massage[i], 670, 210, weapon[0]))
                elif i == 5:
                    my_cards.append(Sprite(massage[i], 1075, 210, weapon[0]))


def get_message(c_s):
    mass = c_s.recv(1024).decode()
    print(mass)
    mass = mass.split(",")
    if mass[0] == "start":
        if mass[1] == "yes":
            return True, False
        else:
            return True, True
    elif mass[0] == "cards":
        mass.pop(0)
        global my_character
        my_character = mass[-1]
        for k in range(6):
            if mass[-1] == sprites[k].name:
                my_character = sprites[k]
        mass.pop(-1)
        print(mass)
        make_cards(mass)
    elif mass[0] == "names":
        mass.pop(0)
        draw_waiting_room(mass, True)
        return False, False
    elif mass[0] == "update":
        for sprite in sprites:
            if mass[1] == sprite.name:
                board.grid[sprite.x][sprite.y].sprite = None
                sprite.x = int(mass[2])
                sprite.y = int(mass[3])
        update()
        draw(board, True, my_cards)
    elif mass[0] == "turn":
        if len(mass) > 1:
            tu = pictures.font.render(mass[1]+"'s turn", True, pictures.Black, pictures.White)
            pictures.screen.blit(tu, (830, 300))
            pygame.display.update()
        else:
            tu = pictures.font.render("your turn", True, pictures.Black, pictures.White)
            pictures.screen.blit(tu, (830, 300))
            pygame.display.update()
            return "u"
    elif mass[0] == "ask":
        mass.pop(0)
        pictures.screen.fill(pictures.Black)
        has_room = False
        has_sus = False
        has_wea = False
        for card in my_cards:
            if card.name == mass[0]:
                pictures.screen.blit(card.img, (200, 100))
                has_room = True
            if card.name == mass[1]:
                pictures.screen.blit(card.img, (350, 100))
                has_sus = True
            if card.name == mass[2]:
                pictures.screen.blit(card.img, (500, 100))
                has_wea = True
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    print(event.pos)
                    if 100 < mouse_y < 275:
                        if has_room:
                            if 200 < mouse_x < 320:
                                c_s.send(("answer," + mass[0]).encode())
                                return
                        if has_sus:
                            if 350 < mouse_x < 470:
                                c_s.send(("answer," + mass[1]).encode())
                                return
                        if has_wea:
                            if 500 < mouse_x < 620:
                                c_s.send(("answer," + mass[2]).encode())
                                return
    elif mass[0] == "answer":
        pictures.screen.fill(pictures.Black)
        if mass[1] == "no":
            answer = pictures.font2.render("no opponent has these cards", True, pictures.Black, pictures.White)
            pictures.screen.blit(answer, (450, 50))
        else:
            for room in pictures.rooms_cards:
                if mass[1] == room[1]:
                    pictures.screen.blit(room[0], (500, 200))
                    pygame.display.flip()
                    time.sleep(2)
            for character in pictures.characters_cards:
                if mass[1] == character[1]:
                    pictures.screen.blit(character[0], (500, 200))
                    pygame.display.flip()
                    time.sleep(2)
            for weapon in pictures.weapons_cards:
                if mass[1] == weapon[1]:
                    pictures.screen.blit(weapon[0], (500, 200))
                    pygame.display.flip()
                    time.sleep(2)
    elif mass[0] == "game over":
        if mass[1] == "yes":
            pictures.screen.fill(pictures.Black)
            massage = pictures.font2.render("you won", True, pictures.Black, pictures.White)
            pictures.screen.blit(massage, (100, 50))
            d_b = pictures.font2.render("Dr. Black was killed in the:", True, pictures.Black, pictures.White)
            pictures.screen.blit(d_b, (50, 285))
            for room in pictures.rooms_cards:
                if mass[2] == room[1]:
                    pictures.screen.blit(room[0], (300, 200))
                    pygame.display.flip()
            for character in pictures.characters_cards:
                if mass[3] == character[1]:
                    mas = pictures.font2.render("by:", True, pictures.Black, pictures.White)
                    pictures.screen.blit(mas, (450, 285))
                    pictures.screen.blit(character[0], (500, 200))
                    pygame.display.flip()
            for weapon in pictures.weapons_cards:
                if mass[4] == weapon[1]:
                    mas = pictures.font2.render("with a:", True, pictures.Black, pictures.White)
                    pictures.screen.blit(mas, (650, 285))
                    pictures.screen.blit(weapon[0], (700, 200))
                    pygame.display.flip()
        elif mass[1] == "no":
            pictures.screen.fill(pictures.Black)
            massage = pictures.font2.render("you lost", True, pictures.Black, pictures.White)
            pictures.screen.blit(massage, (100, 50))
            pygame.display.flip()
            return
        else:
            pictures.screen.fill(pictures.Black)
            massage = pictures.font2.render(mass[1]+" won", True, pictures.Black, pictures.White)
            pictures.screen.blit(massage, (100, 50))
            d_b = pictures.font2.render("Dr. Black was killed in the:", True, pictures.Black, pictures.White)
            pictures.screen.blit(d_b, (50, 285))
            for room in pictures.rooms_cards:
                if mass[2] == room[1]:
                    pictures.screen.blit(room[0], (300, 200))
                    pygame.display.flip()
            for character in pictures.characters_cards:
                if mass[3] == character[1]:
                    mas = pictures.font2.render("by:", True, pictures.Black, pictures.White)
                    pictures.screen.blit(mas, (450, 285))
                    pictures.screen.blit(character[0], (500, 200))
                    pygame.display.flip()
            for weapon in pictures.weapons_cards:
                if mass[4] == weapon[1]:
                    mas = pictures.font2.render("with a:", True, pictures.Black, pictures.White)
                    pictures.screen.blit(mas, (650, 285))
                    pictures.screen.blit(weapon[0], (700, 200))
                    pygame.display.flip()
            return "lose"


def ask(room, soc):
    sus, wea = draw_ask_lists()
    soc.send(("ask," + room + "," + sus + "," + wea).encode())
    get_message(soc)


def accuse(room, soc):
    sus, wea = draw_ask_lists()
    soc.send(("accuse," + room + "," + sus + "," + wea).encode())
    get_message(soc)


def update():
    for sprite in sprites:
        board.grid[sprite.x][sprite.y].sprite = sprite.img


def move(deck):
    rand = random.randint(1, 6)
    rand2 = random.randint(1, 6)
    draw_cube(rand, rand2)
    pygame.display.update()
    rand3 = rand + rand2
    returned = board.roll(my_character, rand3, deck, my_cards)
    if returned:
        return False
    return True


def main():
    client_socket = socket.socket()
    client_socket.connect(("127.0.0.1", 8006))
    lobby = True
    wait = False
    game = True
    played = False
    end = False
    draw_waiting_room()
    while lobby:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lobby = False
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    lobby = False
                    game = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if 100 < mouse_y < 200:
                    if 450 < mouse_x < 500:
                        client_socket.send(("oppo," + str(3)).encode())
                        lobby = False
                        wait = True
                    if 550 < mouse_x < 600:
                        client_socket.send(("oppo," + str(4)).encode())
                        lobby = False
                        wait = True
                    if 650 < mouse_x < 700:
                        client_socket.send(("oppo," + str(5)).encode())
                        lobby = False
                        wait = True
                    if 750 < mouse_x < 800:
                        client_socket.send(("oppo," + str(6)).encode())
                        lobby = False
                        wait = True

                get_message(client_socket)
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                wait = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    wait = False
        begin, played = get_message(client_socket)
        if begin:
            game = True
            wait = False

    deck_up = False
    while game:
        update()
        draw(board, deck_up, my_cards)
        # try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                for i in range(3):
                    for j in range(3):
                        if pictures.rooms[i][j].x <= mouse_x <= pictures.rooms[i][j].x + 80 and \
                                pictures.rooms[i][j].y <= mouse_y <= pictures.rooms[i][j].y + 40:
                            if event.button == 1:
                                pictures.rooms[i][j].img = pictures.check
                            if event.button == 3:
                                pictures.rooms[i][j].img = pictures.red_x
                        try:
                            if pictures.weapons[i][j].x <= mouse_x <= pictures.weapons[i][j].x + 80 and \
                                    pictures.weapons[i][j].y <= mouse_y <= pictures.weapons[i][j].y + 40:
                                if event.button == 1:
                                    pictures.weapons[i][j].img = pictures.check
                                if event.button == 3:
                                    pictures.weapons[i][j].img = pictures.red_x
                            if pictures.suspects[i][j].x <= mouse_x <= pictures.suspects[i][j].x + 100 and \
                                    pictures.suspects[i][j].y <= mouse_y <= pictures.suspects[i][j].y + 40:
                                if event.button == 1:
                                    check = pygame.transform.scale(pictures.check, (100, 40))
                                    pictures.suspects[i][j].img = check
                                if event.button == 3:
                                    red_x = pygame.transform.scale(pictures.red_x, (100, 40))
                                    pictures.suspects[i][j].img = red_x
                        except:
                            pass
                if not played:
                    if event.button == 1:
                        if (pictures.roll_button_pos[0] <= mouse_x <= pictures.roll_button_pos[0] + 50) and \
                                (pictures.roll_button_pos[1] <= mouse_y <= pictures.roll_button_pos[1] + 35):
                            game = move(deck_up)
                            played = True
                            for sprite in sprites:
                                if sprite.name == my_character.name:
                                    sprite.x = my_character.x
                                    sprite.y = my_character.y
                            update()
                            draw(board, deck_up, my_cards)
                            client_socket.send(("update," + my_character.name + "," + str(my_character.x) + "," + str(my_character.y)).encode())
                            time.sleep(1)
                            client_socket.send("end, ".encode())
                        if (pictures.cards_button_pos[0] <= mouse_x <= pictures.cards_button_pos[0] + 100) and \
                                (pictures.cards_button_pos[1] <= mouse_y <= pictures.cards_button_pos[1] + 35):
                            deck_up = True
                            pictures.screen.fill(pictures.Black)
                        if (pictures.accuse_button_pos[0] + 200 >= mouse_x >= pictures.accuse_button_pos[0]) and \
                                (pictures.accuse_button_pos[1] + 35 >= mouse_y >= pictures.accuse_button_pos[1]):
                            if board.grid[my_character.x][my_character.y].ident == "room":
                                accuse(board.grid[my_character.x][my_character.y].room_name, client_socket)
                                update()
                                client_socket.send("end".encode())
                                game = False
                                end = True
                        if (pictures.question_button_pos[0] + 200 >= mouse_x >= pictures.question_button_pos[0]) and \
                                (pictures.question_button_pos[1] + 35 >= mouse_y >= pictures.question_button_pos[1]):
                            if board.grid[my_character.x][my_character.y].ident == "room":
                                ask(board.grid[my_character.x][my_character.y].room_name, client_socket)
                                played = True
                                update()
                                draw(board, deck_up, my_cards)
                                client_socket.send("end".encode())
                        if (pictures.lists_button_pos[0] + 75 >= mouse_x >= pictures.lists_button_pos[0]) and \
                                (pictures.lists_button_pos[1] + 35 >= mouse_y >= pictures.lists_button_pos[1]):
                            deck_up = False
                            draw(board, deck_up, my_cards)
        if played:
            turn = get_message(client_socket)
            if turn == "lose":
                game = False
                end = True
            elif turn == "u":
                played = False

        # except:
            # print("got shut down")
            # client_socket.close()
            # break
    client_socket.close()
    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("end")
                end = False
    # accuse
    # ask


if __name__ == '__main__':
    main()
