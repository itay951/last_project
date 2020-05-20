import random
from Board import *
from pictures import *
from Sprite import *
import socket
import time

while True:
    try:
        client_socket = socket.socket()
        client_socket.connect(("127.0.0.1", 8006))
        client_socket.settimeout(0)
        break
    except:
        pass
TURN = pictures.font.render("Scarlett's turn", True, pictures.Black, pictures.White)
PLAYERS_OUT = False
BEGIN = False
PLAYED = False
LOOSE = False
GAME = False
END = False
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


def get_message():
    # tries to get a message from the server and if it gets a message it checks what it says and doing things accordingly
    global PLAYED, PLAYERS_OUT, BEGIN, LOOSE, my_character, client_socket, GAME, END, TURN
    try:
        mass = client_socket.recv(1024).decode()
    except:
        return
    mass = mass.split(",")
    if mass[0] == "all out":
        pictures.screen.fill(pictures.Black)
        left = pictures.font2.render("rest of the players got out", True, pictures.Black, pictures.White)
        pictures.screen.blit(left, (200*pictures.window_ratio, 100*pictures.window_ratio))
        pygame.display.flip()
        PLAYERS_OUT = True
        return
    if mass[0] == "start":
        if mass[1] == "yes":
            TURN = pictures.font.render("your turn", True, pictures.Black, pictures.White)
            BEGIN = True
            PLAYED = False
            return
        else:
            BEGIN = True
            PLAYED = True
            return
    elif mass[0] == "cards":
        mass.pop(0)
        my_character = mass[-1]
        for k in range(6):
            if mass[-1] == sprites[k].name:
                my_character = sprites[k]
        mass.pop(-1)
        make_cards(mass)
    elif mass[0] == "names":
        mass.pop(0)
        draw_waiting_room(mass, True)
        return
    elif mass[0] == "update":
        for sprite in sprites:
            if mass[1] == sprite.name:
                board.grid[sprite.x][sprite.y].sprite = None
                sprite.x = int(mass[2])
                sprite.y = int(mass[3])
        update()
        draw(board, True, my_cards, TURN)
    elif mass[0] == "turn":
        if mass[1] == "your":
            PLAYED = False
            turn = mass[1] + " turn"
            TURN = pictures.font.render(turn, True, pictures.Black, pictures.White)
            return
        turn = mass[1] + "'s turn"
        TURN = pictures.font.render(turn, True, pictures.Black, pictures.White)
        return
    elif mass[0] == "ask":
        mass.pop(0)
        pictures.screen.fill(pictures.Black)
        has_room = False
        has_sus = False
        has_wea = False
        for card in my_cards:
            if card.name == mass[0]:
                pictures.screen.blit(card.img, (200*pictures.window_ratio, 100*pictures.window_ratio))
                has_room = True
            if card.name == mass[1]:
                pictures.screen.blit(card.img, (350*pictures.window_ratio, 100*pictures.window_ratio))
                has_sus = True
            if card.name == mass[2]:
                pictures.screen.blit(card.img, (500*pictures.window_ratio, 100*pictures.window_ratio))
                has_wea = True
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if 100*pictures.window_ratio < mouse_y < 275*pictures.window_ratio:
                        if has_room:
                            if 200*pictures.window_ratio < mouse_x < 320*pictures.window_ratio:
                                client_socket.send(("answer," + mass[0]).encode())
                                return
                        if has_sus:
                            if 350*pictures.window_ratio < mouse_x < 470*pictures.window_ratio:
                                client_socket.send(("answer," + mass[1]).encode())
                                return
                        if has_wea:
                            if 500*pictures.window_ratio < mouse_x < 620*pictures.window_ratio:
                                client_socket.send(("answer," + mass[2]).encode())
                                return
    elif mass[0] == "answer":
        pictures.screen.fill(pictures.Black)
        if mass[1] == "no":
            answer = pictures.font2.render("no opponent has these cards", True, pictures.Black, pictures.White)
            pictures.screen.blit(answer, (450*pictures.window_ratio, 50*pictures.window_ratio))
            pygame.display.flip()
        else:
            for room in pictures.rooms_cards:
                if mass[1] == room[1]:
                    pictures.screen.blit(room[0], (500*pictures.window_ratio, 200*pictures.window_ratio))
                    pygame.display.flip()
                    time.sleep(2)
            for character in pictures.characters_cards:
                if mass[1] == character[1]:
                    pictures.screen.blit(character[0], (500*pictures.window_ratio, 200*pictures.window_ratio))
                    pygame.display.flip()
                    time.sleep(2)
            for weapon in pictures.weapons_cards:
                if mass[1] == weapon[1]:
                    pictures.screen.blit(weapon[0], (500*pictures.window_ratio, 200*pictures.window_ratio))
                    pygame.display.flip()
                    time.sleep(2)
        client_socket.send("end".encode())
    elif mass[0] == "game over":
        client_socket.send("end".encode())
        GAME = False
        END = True
        if mass[1] == "yes":
            pictures.screen.fill(pictures.Black)
            massage = pictures.font2.render("you won", True, pictures.Black, pictures.White)
            pictures.screen.blit(massage, (100*pictures.window_ratio, 50*pictures.window_ratio))
            d_b = pictures.font2.render("Dr. Black was killed in the:", True, pictures.Black, pictures.White)
            pictures.screen.blit(d_b, (50*pictures.window_ratio, 285*pictures.window_ratio))
            for room in pictures.rooms_cards:
                if mass[2] == room[1]:
                    pictures.screen.blit(room[0], (500*pictures.window_ratio, 200*pictures.window_ratio))
                    pygame.display.flip()
            for character in pictures.characters_cards:
                if mass[3] == character[1]:
                    mas = pictures.font2.render("by:", True, pictures.Black, pictures.White)
                    pictures.screen.blit(mas, (650*pictures.window_ratio, 285*pictures.window_ratio))
                    pictures.screen.blit(character[0], (700*pictures.window_ratio, 200*pictures.window_ratio))
                    pygame.display.flip()
            for weapon in pictures.weapons_cards:
                if mass[4] == weapon[1]:
                    mas = pictures.font2.render("with a:", True, pictures.Black, pictures.White)
                    pictures.screen.blit(mas, (840*pictures.window_ratio, 285*pictures.window_ratio))
                    pictures.screen.blit(weapon[0], (950*pictures.window_ratio, 200*pictures.window_ratio))
                    pygame.display.flip()
        elif mass[1] == "no":
            pictures.screen.fill(pictures.Black)
            massage = pictures.font2.render("you lost", True, pictures.Black, pictures.White)
            pictures.screen.blit(massage, (100*pictures.window_ratio, 50*pictures.window_ratio))
            pygame.display.flip()
            return
        else:
            pictures.screen.fill(pictures.Black)
            massage = pictures.font2.render(mass[1]+" won", True, pictures.Black, pictures.White)
            pictures.screen.blit(massage, (100*pictures.window_ratio, 50*pictures.window_ratio))
            d_b = pictures.font2.render("Dr. Black was killed in the:", True, pictures.Black, pictures.White)
            pictures.screen.blit(d_b, (50*pictures.window_ratio, 285*pictures.window_ratio))
            for room in pictures.rooms_cards:
                if mass[2] == room[1]:
                    pictures.screen.blit(room[0], (500*pictures.window_ratio, 200*pictures.window_ratio))
                    pygame.display.flip()
            for character in pictures.characters_cards:
                if mass[3] == character[1]:
                    mas = pictures.font2.render("by:", True, pictures.Black, pictures.White)
                    pictures.screen.blit(mas, (650*pictures.window_ratio, 285*pictures.window_ratio))
                    pictures.screen.blit(character[0], (700*pictures.window_ratio, 200*pictures.window_ratio))
                    pygame.display.flip()
            for weapon in pictures.weapons_cards:
                if mass[4] == weapon[1]:
                    mas = pictures.font2.render("with a:", True, pictures.Black, pictures.White)
                    pictures.screen.blit(mas, (840*pictures.window_ratio, 285*pictures.window_ratio))
                    pictures.screen.blit(weapon[0], (950*pictures.window_ratio, 200*pictures.window_ratio))
                    pygame.display.flip()
            LOOSE = True
            return


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


def main():
    global PLAYED, BEGIN, PLAYERS_OUT, LOOSE, client_socket, GAME, END, TURN
    lobby = False
    wait = False
    PLAYED = False
    first = True
    while first:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if 400*pictures.window_ratio < mouse_y < 500*pictures.window_ratio:
                    if 100*pictures.window_ratio < mouse_x < 620*pictures.window_ratio:
                        first = False
                        lobby = True
        button = pictures.font3.render("start game", True, pictures.Black, pictures.White)
        pictures.screen.blit(pictures.bg, (0, 0))
        pictures.screen.blit(button, (100*pictures.window_ratio, 400*pictures.window_ratio))
        pygame.display.flip()
    draw_waiting_room()
    while lobby:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lobby = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    lobby = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if 100*pictures.window_ratio < mouse_y < 200*pictures.window_ratio:
                    if 450*pictures.window_ratio < mouse_x < 500*pictures.window_ratio:
                        client_socket.send(("oppo," + str(3)).encode())
                        lobby = False
                        wait = True
                        get_message()
                    if 550*pictures.window_ratio < mouse_x < 600*pictures.window_ratio:
                        client_socket.send(("oppo," + str(4)).encode())
                        lobby = False
                        wait = True
                    if 650*pictures.window_ratio < mouse_x < 700*pictures.window_ratio:
                        client_socket.send(("oppo," + str(5)).encode())
                        lobby = False
                        wait = True
                    if 750*pictures.window_ratio < mouse_x < 800*pictures.window_ratio:
                        client_socket.send(("oppo," + str(6)).encode())
                        lobby = False
                        wait = True

                    if PLAYERS_OUT:
                        lobby = False
                        GAME = False
    while wait:
        get_message()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                wait = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    wait = False

        if PLAYERS_OUT:
            GAME = False
            wait = False
        if BEGIN:
            GAME = True
            wait = False

    deck_up = False
    while GAME:
        update()
        draw(board, deck_up, my_cards, TURN)
        # try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GAME = False
                client_socket.send("end".encode())
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    GAME = False
                    client_socket.send("end".encode())
                    break
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if (pictures.lists_button_pos[0] + 75*pictures.window_ratio >= mouse_x >= pictures.lists_button_pos[0]) and \
                        (pictures.lists_button_pos[1] + 35*pictures.window_ratio >= mouse_y >= pictures.lists_button_pos[1]):
                    deck_up = False
                if (pictures.cards_button_pos[0] <= mouse_x <= pictures.cards_button_pos[0] + 100*window_ratio) and \
                        (pictures.cards_button_pos[1] <= mouse_y <= pictures.cards_button_pos[1] + 35*window_ratio):
                    deck_up = True
                draw(board, deck_up, my_cards, TURN)
                if not deck_up:
                    for i in range(3):
                        for j in range(3):
                            if pictures.rooms[i][j].x <= mouse_x <= pictures.rooms[i][j].x + 80*pictures.window_ratio and \
                                    pictures.rooms[i][j].y <= mouse_y <= pictures.rooms[i][j].y + 40*pictures.window_ratio:
                                if event.button == 1:
                                    pictures.rooms[i][j].img = pictures.check
                                if event.button == 3:
                                    pictures.rooms[i][j].img = pictures.red_x
                            if i < 2:
                                if pictures.weapons[i][j].x <= mouse_x <= pictures.weapons[i][j].x + 80*pictures.window_ratio and \
                                        pictures.weapons[i][j].y <= mouse_y <= pictures.weapons[i][j].y + 40*pictures.window_ratio:
                                    if event.button == 1:
                                        pictures.weapons[i][j].img = pictures.check
                                    if event.button == 3:
                                        pictures.weapons[i][j].img = pictures.red_x
                                if pictures.suspects[i][j].x <= mouse_x <= pictures.suspects[i][j].x + 100*pictures.window_ratio and \
                                        pictures.suspects[i][j].y <= mouse_y <= pictures.suspects[i][j].y + 40*pictures.window_ratio:
                                    if event.button == 1:
                                        check = pygame.transform.scale(pictures.check, (int(100*pictures.window_ratio), int(40*pictures.window_ratio)))
                                        pictures.suspects[i][j].img = check
                                    if event.button == 3:
                                        red_x = pygame.transform.scale(pictures.red_x, (int(100*pictures.window_ratio), int(40*pictures.window_ratio)))
                                        pictures.suspects[i][j].img = red_x
                if not PLAYED:
                    if event.button == 1:
                        if (pictures.roll_button_pos[0] <= mouse_x <= pictures.roll_button_pos[0] + 50*pictures.window_ratio) and \
                                (pictures.roll_button_pos[1] <= mouse_y <= pictures.roll_button_pos[1] + 35*pictures.window_ratio):
                            GAME = move(deck_up)
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
                        if (pictures.accuse_button_pos[0] + 200*pictures.window_ratio >= mouse_x >= pictures.accuse_button_pos[0]) and \
                                (pictures.accuse_button_pos[1] + 35*window_ratio >= mouse_y >= pictures.accuse_button_pos[1]):
                            if board.grid[my_character.x][my_character.y].ident == "room":
                                accuse(board.grid[my_character.x][my_character.y].room_name)
                                if PLAYERS_OUT:
                                    pictures.screen.fill(pictures.Black)
                                    mas = pictures.font2.render("all other players left game", True, pictures.Black, pictures.White)
                                    pictures.screen.blit(mas, (450*pictures.window_ratio, 50*pictures.window_ratio))
                                    pygame.display.flip()
                                else:
                                    PLAYED = True
                        if (pictures.question_button_pos[0] + 200*window_ratio >= mouse_x >= pictures.question_button_pos[0]) and \
                                (pictures.question_button_pos[1] + 35*window_ratio >= mouse_y >= pictures.question_button_pos[1]):
                            if board.grid[my_character.x][my_character.y].ident == "room":
                                ask(board.grid[my_character.x][my_character.y].room_name)
                                if PLAYERS_OUT:
                                    GAME = False
                                    END = True
                                    pictures.screen.fill(pictures.Black)
                                    mas = pictures.font2.render("all other players left game", True, pictures.Black,
                                                                pictures.White)
                                    pictures.screen.blit(mas, (450*pictures.window_ratio, 50*pictures.window_ratio))
                                    pygame.display.flip()
                                else:
                                    PLAYED = True

        if PLAYED:
            get_message()
            if PLAYERS_OUT:
                GAME = False
                pictures.screen.fill(pictures.Black)
                mas = pictures.font2.render("all other players left game", True, pictures.Black, pictures.White)
                pictures.screen.blit(mas, (450*pictures.window_ratio, 50*pictures.window_ratio))
                pygame.display.flip()
                END = True
            if LOOSE:
                GAME = False
                END = True

        # except:
            # break
    client_socket.close()
    while END:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                END = False


if __name__ == '__main__':
    main()
