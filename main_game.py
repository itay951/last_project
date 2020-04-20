import random
from Board import *
from pictures import *
from Sprite import *
import socket


board = Board()
pictures = pictures()
sprites = []
sprites.append(Sprite("red", 16, 0, pictures.red))
sprites.append(Sprite("yellow", 23, 7, pictures.yellow))
sprites.append(Sprite("green", 9, 24, pictures.green))
sprites.append(Sprite("purple", 0, 5, pictures.purple))
sprites.append(Sprite("blue", 0, 18, pictures.blue))
sprites.append(Sprite("white", 14, 24, pictures.white))
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
        if massage[i] == "Miss Scarlett":
            my_cards.append(Sprite(massage[i], 670 + 135 * i, 35, pictures.miss_scarlet_card))
            if i == 4:
                my_cards.append(Sprite(massage[i], 670, 210, pictures.miss_scarlet_card))
            if i == 5:
                my_cards.append(Sprite(massage[i], 1075, 210, pictures.miss_scarlet_card))
        if massage[i] == "Rev. Green":
            my_cards.append(Sprite(massage[i], 670 + 135 * i, 35, pictures.rev_green_card))
            if i == 4:
                my_cards.append(Sprite(massage[i], 670, 210, pictures.rev_green_card))
            if i == 5:
                my_cards.append(Sprite(massage[i], 1075, 210, pictures.rev_green_card))
        if massage[i] == "Colonel Mustard":
            my_cards.append(Sprite(massage[i], 670 + 135 * i, 35, pictures.col_mustard_card))
            if i == 4:
                my_cards.append(Sprite(massage[i], 670, 210, pictures.col_mustard_card))
            if i == 5:
                my_cards.append(Sprite(massage[i], 1075, 210, pictures.col_mustard_card))
        if massage[i] == "Mrs. Peacock":
            my_cards.append(Sprite(massage[i], 670 + 135 * i, 35, pictures.mrs_peacock_card))
            if i == 4:
                my_cards.append(Sprite(massage[i], 670, 210, pictures.mrs_peacock_card))
            if i == 5:
                my_cards.append(Sprite(massage[i], 1075, 210, pictures.mrs_peacock_card))
        if massage[i] == "Professor Plum":
            my_cards.append(Sprite(massage[i], 670 + 135 * i, 35, pictures.professor_plum_card))
            if i == 4:
                my_cards.append(Sprite(massage[i], 670, 210, pictures.professor_plum_card))
            if i == 5:
                my_cards.append(Sprite(massage[i], 1075, 210, pictures.professor_plum_card))
        if massage[i] == "Mrs. White":
            my_cards.append(Sprite(massage[i], 670 + 135 * i, 35, pictures.mrs_white_card))
            if i == 4:
                my_cards.append(Sprite(massage[i], 670, 210, pictures.mrs_white_card))
            if i == 5:
                my_cards.append(Sprite(massage[i], 1075, 210, pictures.mrs_white_card))
        if massage[i] == "dagger":
            my_cards.append(Sprite(massage[i], 670 + 135 * i, 35, pictures.dagger_card))
            if i == 4:
                my_cards.append(Sprite(massage[i], 670, 210, pictures.dagger_card))
            if i == 5:
                my_cards.append(Sprite(massage[i], 1075, 210, pictures.dagger_card))
        if massage[i] == "lead pipe":
            my_cards.append(Sprite(massage[i], 670 + 135 * i, 35, pictures.lead_pipe_card))
            if i == 4:
                my_cards.append(Sprite(massage[i], 670, 210, pictures.lead_pipe_card))
            if i == 5:
                my_cards.append(Sprite(massage[i], 1075, 210, pictures.lead_pipe_card))
        if massage[i] == "candlestick":
            my_cards.append(Sprite(massage[i], 670 + 135 * i, 35, pictures.candlestick_card))
            if i == 4:
                my_cards.append(Sprite(massage[i], 670, 210, pictures.candlestick_card))
            if i == 5:
                my_cards.append(Sprite(massage[i], 1075, 210, pictures.candlestick_card))
        if massage[i] == "revolver":
            my_cards.append(Sprite(massage[i], 670 + 135 * i, 35, pictures.gun_card))
            if i == 4:
                my_cards.append(Sprite(massage[i], 670, 210, pictures.gun_card))
            if i == 5:
                my_cards.append(Sprite(massage[i], 1075, 210, pictures.gun_card))
        if massage[i] == "rope":
            my_cards.append(Sprite(massage[i], 670 + 135 * i, 35, pictures.rope_card))
            if i == 4:
                my_cards.append(Sprite(massage[i], 670, 210, pictures.rope_card))
            if i == 5:
                my_cards.append(Sprite(massage[i], 1075, 210, pictures.rope_card))
        if massage[i] == "wrench":
            my_cards.append(Sprite(massage[i], 670 + 135 * i, 35, pictures.wrench_card))
            if i == 4:
                my_cards.append(Sprite(massage[i], 670, 210, pictures.wrench_card))
            if i == 5:
                my_cards.append(Sprite(massage[i], 1075, 210, pictures.wrench_card))
        if massage[i] == "study":
            my_cards.append(Sprite(massage[i], 670 + 135 * i, 35, pictures.study_card))
            if i == 4:
                my_cards.append(Sprite(massage[i], 670, 210, pictures.study_card))
            if i == 5:
                my_cards.append(Sprite(massage[i], 1075, 210, pictures.study_card))
        if massage[i] == "library":
            my_cards.append(Sprite(massage[i], 670 + 135 * i, 35, pictures.library_card))
            if i == 4:
                my_cards.append(Sprite(massage[i], 670, 210, pictures.library_card))
            if i == 5:
                my_cards.append(Sprite(massage[i], 1075, 210, pictures.library_card))
        if massage[i] == "billiard room":
            my_cards.append(Sprite(massage[i], 670 + 135 * i, 35, pictures.billiard_card))
            if i == 4:
                my_cards.append(Sprite(massage[i], 670, 210, pictures.billiard_card))
            if i == 5:
                my_cards.append(Sprite(massage[i], 1075, 210, pictures.billiard_card))
        if massage[i] == "conservatory":
            my_cards.append(Sprite(massage[i], 670 + 135 * i, 35, pictures.conservatory_card))
            if i == 4:
                my_cards.append(Sprite(massage[i], 670, 210, pictures.conservatory_card))
            if i == 5:
                my_cards.append(Sprite(massage[i], 1075, 210, pictures.conservatory_card))
        if massage[i] == "hall":
            my_cards.append(Sprite(massage[i], 670 + 135 * i, 35, pictures.hall_card))
            if i == 4:
                my_cards.append(Sprite(massage[i], 670, 210, pictures.hall_card))
            if i == 5:
                my_cards.append(Sprite(massage[i], 1075, 210, pictures.hall_card))
        if massage[i] == "ballroom":
            my_cards.append(Sprite(massage[i], 670 + 135 * i, 35, pictures.ballroom_card))
            if i == 4:
                my_cards.append(Sprite(massage[i], 670, 210, pictures.ballroom_card))
            if i == 5:
                my_cards.append(Sprite(massage[i], 1075, 210, pictures.ballroom_card))
        if massage[i] == "lounge":
            my_cards.append(Sprite(massage[i], 670 + 135 * i, 35, pictures.lounge_card))
            if i == 4:
                my_cards.append(Sprite(massage[i], 670, 210, pictures.lounge_card))
            if i == 5:
                my_cards.append(Sprite(massage[i], 1075, 210, pictures.lounge_card))
        if massage[i] == "dining room":
            my_cards.append(Sprite(massage[i], 670 + 135 * i, 35, pictures.dining_card))
            if i == 4:
                my_cards.append(Sprite(massage[i], 670, 210, pictures.dining_card))
            if i == 5:
                my_cards.append(Sprite(massage[i], 1075, 210, pictures.dining_card))
        if massage[i] == "kitchen":
            my_cards.append(Sprite(massage[i], 670 + 135 * i, 35, pictures.kitchen_card))
            if i == 4:
                my_cards.append(Sprite(massage[i], 670, 210, pictures.kitchen_card))
            if i == 5:
                my_cards.append(Sprite(massage[i], 1075, 210, pictures.kitchen_card))


def get_message(c_s):
    mass = c_s.recv(1024).decode()
    print(mass)
    mass = mass.split(",")
    if mass[0] == "start":
        if mass[1] == "yes":
            return True, False
        else:
            return True, True
    if mass[0] == "cards":
        mass.pop(0)
        global my_character
        my_character = mass[-1]
        if my_character == "Miss Scarlett":
            my_character = sprites[0]
        elif my_character == "Colonel Mustard":
            my_character = sprites[1]
        elif my_character == "Rev. Green":
            my_character = sprites[2]
        elif my_character == "Professor Plum":
            my_character = sprites[3]
        elif my_character == "Mrs. Peacock":
            my_character = sprites[4]
        elif my_character == "Mrs. White":
            my_character = sprites[5]
        mass.pop(-1)
        make_cards(mass)
    if mass[0] == "names":
        mass.pop(0)
        draw_waiting_room(mass, True)
        return False, False
    if mass[0] == "update":
        for sprite in sprites:
            if mass[1] == sprite.name:
                board.grid[sprite.x][sprite.y] = None
                sprite.x = int(mass[2])
                sprite.y = int(mass[3])
        update()
        draw(board, True, my_cards)


def ask():
    pass


def accuse():
    pass


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
    """for i in range(board.grid_size_x):
        for j in range(board.grid_size_y):
            if board.grid[i][j].sprite is red.img:
                red.x = i
                red.y = j"""
    return True


def main():
    client_socket = socket.socket()
    client_socket.connect(("127.0.0.1", 8006))
    lobby = True
    wait = False
    game = False
    played = False
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
                            client_socket.send(("update" + my_character.name + "," + str(my_character.x) + "," + str(my_character.y)).encode())
                        if (pictures.cards_button_pos[0] <= mouse_x <= pictures.cards_button_pos[0] + 100) and \
                                (pictures.cards_button_pos[1] <= mouse_y <= pictures.cards_button_pos[1] + 35):
                            deck_up = True
                            pictures.screen.fill(pictures.Black)
                        if (pictures.accuse_button_pos[0] + 200 >= mouse_x >= pictures.accuse_button_pos[0]) and \
                                (pictures.accuse_button_pos[1] + 35 >= mouse_y >= pictures.accuse_button_pos[1]):
                            accuse()
                            played = True
                            client_socket.send(("update" + my_character.name + "," + str(my_character.x) + "," + str(my_character.y)).encode())
                        if (pictures.question_button_pos[0] + 200 >= mouse_x >= pictures.question_button_pos[0]) and \
                                (pictures.question_button_pos[1] + 35 >= mouse_y >= pictures.question_button_pos[1]):
                            ask()
                            played = True
                            client_socket.send(("update" + my_character.name + "," + str(my_character.x) + "," + str(my_character.y)).encode())
                        if (pictures.lists_button_pos[0] + 75 >= mouse_x >= pictures.lists_button_pos[0]) and \
                                (pictures.lists_button_pos[1] + 35 >= mouse_y >= pictures.lists_button_pos[1]):
                            deck_up = False
                            draw(board, deck_up, my_cards)
                else:
                    get_message(client_socket)
                    print()

        # except:
            # print("got shut down")
            # break


if __name__ == '__main__':
    main()
