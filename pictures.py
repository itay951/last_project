import pygame
import ctypes
import os
from List_Object import *
pygame.init()
user32 = ctypes.windll.user32
place_win = (0, 30)
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % place_win


class pictures:

    # colors
    Black = (0, 0, 0)
    Grey = (211, 211, 211)
    White = (255, 255, 255)

    # screen
    screensizex = user32.GetSystemMetrics(0)
    screensizey = user32.GetSystemMetrics(1)
    screen = pygame.display.set_mode((screensizex, screensizey), pygame.RESIZABLE)
    pygame.display.set_caption("cluedo")
    screen.fill(Black)
    window_ratio = screensizex/1280

    bg = pygame.image.load("game_pieces/first_page_b_g.jpg")
    bg = pygame.transform.scale(bg, (screensizex, screensizey))

    # game pieces
    empty = pygame.image.load("game_pieces/empty.png")
    grey = pygame.image.load("game_pieces/grey_block.png")
    white_block = pygame.image.load("game_pieces/white_block.png")
    white_block = pygame.transform.scale(white_block, (int(80*window_ratio), int(40*window_ratio)))
    white_block2 = pygame.image.load("game_pieces/white_block.png")
    white_block2 = pygame.transform.scale(white_block2, (int(100*window_ratio), int(40*window_ratio)))

    # characters
    yellow = pygame.image.load("game_pieces/crl_mustard.png")
    yellow = pygame.transform.scale(yellow, (int(30*window_ratio), int(30*window_ratio)))
    red = pygame.image.load("game_pieces/miss_scarlet.png")
    red = pygame.transform.scale(red, (int(30*window_ratio), int(30*window_ratio)))
    green = pygame.image.load("game_pieces/mr_green.png")
    green = pygame.transform.scale(green, (int(30*window_ratio), int(30*window_ratio)))
    purple = pygame.image.load("game_pieces/prof_plum.png")
    purple = pygame.transform.scale(purple, (int(30*window_ratio), int(30*window_ratio)))
    white = pygame.image.load("game_pieces/mrs_white.png")
    white = pygame.transform.scale(white, (int(30*window_ratio), int(30*window_ratio)))
    blue = pygame.image.load("game_pieces/ms_peacock.png")
    blue = pygame.transform.scale(blue, (int(30*window_ratio), int(30*window_ratio)))

    # weapons
    dagger = pygame.image.load("game_pieces/dagger.png")
    dagger = pygame.transform.scale(dagger, (int(60*window_ratio), int(30*window_ratio)))
    rope = pygame.image.load("game_pieces/rope.png")
    rope = pygame.transform.scale(rope, (int(60*window_ratio), int(30*window_ratio)))
    wrench = pygame.image.load("game_pieces/wrench.png")
    wrench = pygame.transform.scale(wrench, (int(60*window_ratio), int(30*window_ratio)))
    pipe = pygame.image.load("game_pieces/lead_pipe.png")
    pipe = pygame.transform.scale(pipe, (int(60*window_ratio), int(30*window_ratio)))
    gun = pygame.image.load("game_pieces/gun.png")
    gun = pygame.transform.scale(gun, (int(60*window_ratio), int(30*window_ratio)))
    candlestick = pygame.image.load("game_pieces/candlestick.png")
    candlestick = pygame.transform.scale(candlestick, (int(60*window_ratio), int(30*window_ratio)))

    # board parts
    tile = pygame.image.load("game_pieces/board.jpg")
    tile = pygame.transform.scale(tile, (int(1078*0.6*window_ratio), int(1097*0.6*window_ratio)))

    # doors
    # study
    study_door = pygame.image.load("game_pieces/study_door.png")
    study_door = pygame.transform.scale(study_door, (int(100*0.5*window_ratio), int(100*0.5*window_ratio)))

    # library
    blue_library_door = pygame.image.load("game_pieces/blue_library_door.png")
    blue_library_door = pygame.transform.rotozoom(blue_library_door, 0, 0.5*window_ratio)
    red_library_door = pygame.image.load("game_pieces/red_library_door.png")
    red_library_door = pygame.transform.rotozoom(red_library_door, 0, 0.5*window_ratio)

    # billiard
    blue_billiard_door = pygame.image.load("game_pieces/blue_billiard_door.png")
    blue_billiard_door = pygame.transform.rotozoom(blue_billiard_door, 0, 0.5*window_ratio)
    red_billiard_door = pygame.image.load("game_pieces/red_billiard_door.png")
    red_billiard_door = pygame.transform.rotozoom(red_billiard_door, 0, 0.5*window_ratio)

    # conservatory
    conservatory_door = pygame.image.load("game_pieces/conservatory_door.png")
    conservatory_door = pygame.transform.rotozoom(conservatory_door, 0, 0.5*window_ratio)

    # hall
    blue_hall_door = pygame.image.load("game_pieces/blue_hall_door.png")
    blue_hall_door = pygame.transform.rotozoom(blue_hall_door, 0, 0.5*window_ratio)
    red_hall_door = pygame.image.load("game_pieces/red_hall_door.png")
    red_hall_door = pygame.transform.rotozoom(red_hall_door, 0, 0.5*window_ratio)
    green_hall_door = pygame.image.load("game_pieces/green_hall_door.png")
    green_hall_door = pygame.transform.rotozoom(green_hall_door, 0, 0.5*window_ratio)

    # ballroom
    blue_ball_door = pygame.image.load("game_pieces/blue_ball_door.png")
    blue_ball_door = pygame.transform.rotozoom(blue_ball_door, 0, 0.5*window_ratio)
    red_ball_door = pygame.image.load("game_pieces/red_ball_door.png")
    red_ball_door = pygame.transform.rotozoom(red_ball_door, 0, 0.5*window_ratio)
    green_ball_door = pygame.image.load("game_pieces/green_ball_door.png")
    green_ball_door = pygame.transform.rotozoom(green_ball_door, 0, 0.5*window_ratio)
    yellow_ball_door = pygame.image.load("game_pieces/yellow_ball_door.png")
    yellow_ball_door = pygame.transform.rotozoom(yellow_ball_door, 0, 0.5*window_ratio)

    # lounge
    lounge_door = pygame.image.load("game_pieces/lounge_door.png")
    lounge_door = pygame.transform.rotozoom(lounge_door, 0, 0.5*window_ratio)

    # dining room
    blue_dining_door = pygame.image.load("game_pieces/blue_dining_door.png")
    blue_dining_door = pygame.transform.rotozoom(blue_dining_door, 0, 0.5*window_ratio)
    red_dinning_door = pygame.image.load("game_pieces/red_dining_door.png")
    red_dinning_door = pygame.transform.rotozoom(red_dinning_door, 0, 0.5*window_ratio)

    # kitchen
    kitchen_door = pygame.image.load("game_pieces/kitchen_door.png")
    kitchen_door = pygame.transform.rotozoom(kitchen_door, 0, 0.5*window_ratio)

    # clue lists
    font = pygame.font.Font('freesansbold.ttf', int(12*window_ratio))

    # marks
    check = pygame.image.load("game_pieces/green_check.png")
    check = pygame.transform.scale(check, (int(80*window_ratio), int(40*window_ratio)))
    red_x = pygame.image.load("game_pieces/red_x.png")
    red_x = pygame.transform.scale(red_x, (int(80*window_ratio), int(40*window_ratio)))

    # rooms
    rooms = [[], [], []]
    for i in range(3):
        for j in range(3):
            rooms[i].append(List_Object(825*window_ratio + i * 85*window_ratio, 200*window_ratio + j * 45*window_ratio))
    rooms_names = ["study", "library", "billiard room", "conservatory", "hall", "ballroom", "lounge", "dining room",
                   "kitchen"]
    # weapons
    weapons = [[], []]
    for i in range(3):
        for j in range(2):
            weapons[j].append(List_Object(1000*window_ratio + i * 85*window_ratio, 50*window_ratio + j * 45*window_ratio))
    weapons_names = ["dagger", "lead pipe", "candlestick", "revolver", "rope", "wrench"]

    # suspects
    suspects = [[], []]
    for i in range(3):
        for j in range(2):
            suspects[j].append(List_Object(670*window_ratio + i * 105*window_ratio, 50*window_ratio + j * 45*window_ratio))
    suspects_names = ["Miss Scarlett", "Rev. Green", "Colonel Mustard", "Mrs. Peacock", "Professor Plum", "Mrs. White"]

    grey = pygame.transform.scale(grey, (int(600*window_ratio), int(620*window_ratio)))
    k = 0
    for i in range(3):
        for j in range(3):
            rooms[i][j].word = font.render(rooms_names[k], True, Black, White)
            rooms[i][j].bg = white_block
            if i < 2:
                weapons[i][j].bg = white_block
                weapons[i][j].word = font.render(weapons_names[k], True, Black, White)
                suspects[i][j].bg = white_block2
                suspects[i][j].word = font.render(suspects_names[k], True, Black, White)
            k += 1

    # buttons
    font2 = pygame.font.Font('freesansbold.ttf', int(32*window_ratio))
    roll = font2.render('roll', True, Black, White)
    roll_button = roll.get_rect()
    question = font2.render('suggestion', True, Black, White)
    question_button = question.get_rect()
    accuse = font2.render('accusation', True, Black, White)
    accuse_button = question.get_rect()
    cards = font2.render('cards', True, Black, White)
    lists = font2.render('lists', True, Black, White)
    turn = font.render("Miss Scarlett's turn", True, Black, White)

    # cards
    # rooms
    ballroom_card = pygame.image.load("game_pieces/ballroom_card.png")
    ballroom_card = pygame.transform.rotozoom(ballroom_card, 0, 0.25*window_ratio)
    billiard_card = pygame.image.load("game_pieces/billiard_card.png")
    billiard_card = pygame.transform.rotozoom(billiard_card, 0, 0.25*window_ratio)
    conservatory_card = pygame.image.load("game_pieces/conservatory_card.png")
    conservatory_card = pygame.transform.rotozoom(conservatory_card, 0, 0.25*window_ratio)
    dining_card = pygame.image.load("game_pieces/dining_card.png")
    dining_card = pygame.transform.rotozoom(dining_card, 0, 0.25*window_ratio)
    hall_card = pygame.image.load("game_pieces/hall_card.png")
    hall_card = pygame.transform.rotozoom(hall_card, 0, 0.25*window_ratio)
    kitchen_card = pygame.image.load("game_pieces/kitchen_card.png")
    kitchen_card = pygame.transform.rotozoom(kitchen_card, 0, 0.25*window_ratio)
    library_card = pygame.image.load("game_pieces/library_card.png")
    library_card = pygame.transform.rotozoom(library_card, 0, 0.25*window_ratio)
    lounge_card = pygame.image.load("game_pieces/lounge_card.png")
    lounge_card = pygame.transform.rotozoom(lounge_card, 0, 0.25*window_ratio)
    study_card = pygame.image.load("game_pieces/study_card.png")
    study_card = pygame.transform.rotozoom(study_card, 0, 0.25*window_ratio)

    # characters
    col_mustard_card = pygame.image.load("game_pieces/col_mustard_card.png")
    col_mustard_card = pygame.transform.rotozoom(col_mustard_card, 0, 0.25*window_ratio)
    miss_scarlet_card = pygame.image.load("game_pieces/miss_scarlet_card.png")
    miss_scarlet_card = pygame.transform.rotozoom(miss_scarlet_card, 0, 0.25*window_ratio)
    mrs_peacock_card = pygame.image.load("game_pieces/mrs_peacock_card.png")
    mrs_peacock_card = pygame.transform.rotozoom(mrs_peacock_card, 0, 0.25*window_ratio)
    mrs_white_card = pygame.image.load("game_pieces/mrs_white_card.png")
    mrs_white_card = pygame.transform.rotozoom(mrs_white_card, 0, 0.25*window_ratio)
    professor_plum_card = pygame.image.load("game_pieces/professor_plum_card.png")
    professor_plum_card = pygame.transform.rotozoom(professor_plum_card, 0, 0.25*window_ratio)
    rev_green_card = pygame.image.load("game_pieces/rev_green_card.png")
    rev_green_card = pygame.transform.rotozoom(rev_green_card, 0, 0.25*window_ratio)

    # weapons
    candlestick_card = pygame.image.load("game_pieces/candlestick_card.png")
    candlestick_card = pygame.transform.rotozoom(candlestick_card, 0, 0.25*window_ratio)
    dagger_card = pygame.image.load("game_pieces/dagger_card.png")
    dagger_card = pygame.transform.rotozoom(dagger_card, 0, 0.25*window_ratio)
    gun_card = pygame.image.load("game_pieces/revolver_card.png")
    gun_card = pygame.transform.rotozoom(gun_card, 0, 0.25*window_ratio)
    lead_pipe_card = pygame.image.load("game_pieces/lead_pipe_card.png")
    lead_pipe_card = pygame.transform.rotozoom(lead_pipe_card, 0, 0.25*window_ratio)
    rope_card = pygame.image.load("game_pieces/rope_card.png")
    rope_card = pygame.transform.rotozoom(rope_card, 0, 0.25*window_ratio)
    wrench_card = pygame.image.load("game_pieces/wrench_card.png")
    wrench_card = pygame.transform.rotozoom(wrench_card, 0, 0.25*window_ratio)

    characters_cards = [(miss_scarlet_card, "Miss Scarlett"), (rev_green_card, "Rev. Green"),
                        (col_mustard_card, "Colonel Mustard"), (mrs_peacock_card, "Mrs. Peacock"),
                        (professor_plum_card, "Professor Plum"), (mrs_white_card, "Mrs. White")]
    weapons_cards = [(dagger_card, "dagger"), (lead_pipe_card, "lead pipe"),
                     (candlestick_card, "candlestick"), (rope_card, "rope"),
                     (gun_card, "revolver"), (wrench_card, "wrench")]
    rooms_cards = [(ballroom_card, "ballroom"), (billiard_card, "billiard room"), (conservatory_card, "conservatory"),
                   (dining_card, "dining room"), (hall_card, "hall"), (kitchen_card, "kitchen"),
                   (library_card, "library"), (lounge_card, "lounge"), (study_card, "study")]

    # cubes
    cube_1 = pygame.image.load("game_pieces/cube_1.png")
    cube_1 = pygame.transform.rotozoom(cube_1, 0, 0.5*window_ratio)
    cube_2 = pygame.image.load("game_pieces/cube_1.png")
    cube_2 = pygame.transform.rotozoom(cube_2, 0, 0.5*window_ratio)

    # positions
    roll_button_pos = (screensizex * 5 // 9, screensizey * 5 // 8)
    question_button_pos = (screensizex * 6 // 10 + 15, screensizey * 5 // 8)
    accuse_button_pos = (screensizex * 7 // 9 + 30, screensizey * 5 // 8)
    cards_button_pos = (screensizex * 6 // 10 + 105*window_ratio, screensizey * 4 // 8 + 10)
    lists_button_pos = (screensizex * 6 // 10 + 225*window_ratio, screensizey * 4 // 8 + 10)
    cube1_pos = (screensizex * 4 // 7 + 30, screensizey * 6 // 8 - 30)
    cube2_pos = (screensizex * 6 // 8 + 40, screensizey * 6 // 8 - 30)

    # pre game
    font3 = pygame.font.Font('freesansbold.ttf', int(100*window_ratio))
    quest = font2.render("How many opponents do you want to play with", True, Black, White)
    oppo_amount = []
    for i in range(4):
        oppo_amount.append(List_Object(450*window_ratio + 100*i*window_ratio, 100*window_ratio, font3.render(str(i+3), True, Black, White)))


def draw(board, deck, cards):
    # output to the screen
    pictures.screen.fill(pictures.Black)
    pictures.screen.blit(pictures.tile, (0, 0))
    pictures.screen.blit(pictures.grey, (660*pictures.window_ratio, 10*pictures.window_ratio))
    if deck:
        for card in cards:
            pictures.screen.blit(card.img, (card.x, card.y))
    for x in range(board.grid_size_x):
        for y in range(board.grid_size_y):
            if not deck:
                if x < 3 and y < 3:
                    pictures.screen.blit(pictures.rooms[x][y].bg, (pictures.rooms[x][y].x, pictures.rooms[x][y].y))
                    pictures.screen.blit(pictures.rooms[x][y].word, (pictures.rooms[x][y].x, pictures.rooms[x][y].y+15))
                    if pictures.rooms[x][y].img is not None:
                        pictures.screen.blit(pictures.rooms[x][y].img, (pictures.rooms[x][y].x, pictures.rooms[x][y].y))
                    if x < 2:
                        pictures.screen.blit(pictures.weapons[x][y].bg,
                                             (pictures.weapons[x][y].x, pictures.weapons[x][y].y))
                        pictures.screen.blit(pictures.weapons[x][y].word,
                                             (pictures.weapons[x][y].x, pictures.weapons[x][y].y + 15))
                        pictures.screen.blit(pictures.suspects[x][y].bg,
                                             (pictures.suspects[x][y].x, pictures.suspects[x][y].y))
                        pictures.screen.blit(pictures.suspects[x][y].word,
                                             (pictures.suspects[x][y].x, pictures.suspects[x][y].y + 15))
                        if pictures.suspects[x][y].img is not None:
                            pictures.screen.blit(pictures.suspects[x][y].img, (pictures.suspects[x][y].x, pictures.suspects[x][y].y))
                        if pictures.weapons[x][y].img is not None:
                            pictures.screen.blit(pictures.weapons[x][y].img, (pictures.weapons[x][y].x, pictures.weapons[x][y].y))
            if board.grid[x][y].sprite is not None:
                pictures.screen.blit(board.grid[x][y].sprite, (board.grid[x][y].x, board.grid[x][y].y))
    pictures.screen.blit(pictures.roll, pictures.roll_button_pos)
    pictures.screen.blit(pictures.question, pictures.question_button_pos)
    pictures.screen.blit(pictures.accuse, pictures.accuse_button_pos)
    pictures.screen.blit(pictures.cards, pictures.cards_button_pos)
    pictures.screen.blit(pictures.lists, pictures.lists_button_pos)
    pictures.screen.blit(pictures.cube_1, pictures.cube1_pos)
    pictures.screen.blit(pictures.cube_2, pictures.cube2_pos)
    pictures.screen.blit(pictures.turn, (670*pictures.window_ratio, 400*pictures.window_ratio))
    pygame.display.flip()


def draw_cube(cube1, cube2):
    pictures.cube_1 = pygame.image.load("game_pieces/cube_" + str(cube1) + ".png")
    pictures.cube_1 = pygame.transform.rotozoom(pictures.cube_1, 0, 0.5*pictures.window_ratio)
    pictures.cube_2 = pygame.image.load("game_pieces/cube_" + str(cube2) + ".png")
    pictures.cube_2 = pygame.transform.rotozoom(pictures.cube_2, 0, 0.5*pictures.window_ratio)


def draw_waiting_room(characters=None, waiting=False):
    pictures.screen.fill(pictures.Black)
    if waiting:
        for i in range(len(characters)):
            if characters[i] == "Miss Scarlett":
                characters[i] = pictures.miss_scarlet_card
            elif characters[i] == "Rev. Green":
                characters[i] = pictures.rev_green_card
            elif characters[i] == "Colonel Mustard":
                characters[i] = pictures.col_mustard_card
            elif characters[i] == "Mrs. Peacock":
                characters[i] = pictures.mrs_peacock_card
            elif characters[i] == "Professor Plum":
                characters[i] = pictures.professor_plum_card
            elif characters[i] == "Mrs. White":
                characters[i] = pictures.mrs_white_card
        for i in range(len(characters)):
            pictures.screen.blit(characters[i], (200*pictures.window_ratio + 150*i*pictures.window_ratio, 100*pictures.window_ratio))
        pictures.quest = pictures.font2.render("Waiting for opponents", True, pictures.Black, pictures.White)
        pictures.screen.blit(pictures.quest, (450*pictures.window_ratio, 50*pictures.window_ratio))
    else:
        pictures.screen.blit(pictures.quest, (300*pictures.window_ratio, 50*pictures.window_ratio))
        for i in range(4):
            pictures.screen.blit(pictures.oppo_amount[i].img, (pictures.oppo_amount[i].x, pictures.oppo_amount[i].y))
    pygame.display.flip()


def draw_ask_lists():
    # output to the screen the cards when you choose to ask or accuse
    pictures.screen.fill(pictures.Black)
    chosen_c = ""
    chosen_w = ""
    c_1 = True
    c_2 = True
    while c_1 or c_2:
        for i in range(6):
            pictures.screen.blit(pictures.characters_cards[i][0], (200*pictures.window_ratio + 150*pictures.window_ratio*i, 100*pictures.window_ratio))
            pictures.screen.blit(pictures.weapons_cards[i][0], (200*pictures.window_ratio + 150 * i*pictures.window_ratio, 300*pictures.window_ratio))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                for i in range(6):
                    if c_1:
                        if 100*pictures.window_ratio < mouse_y < 275*pictures.window_ratio:
                            if 200*pictures.window_ratio + 150*i*pictures.window_ratio < mouse_x < 320*pictures.window_ratio + 150*i*pictures.window_ratio:
                                chosen_c = pictures.characters_cards[i][1]
                                c_1 = False
                    if c_2:
                        if 300*pictures.window_ratio < mouse_y < 475*pictures.window_ratio:
                            if 200*pictures.window_ratio + 150*i*pictures.window_ratio < mouse_x < 320*pictures.window_ratio + 150*i*pictures.window_ratio:
                                chosen_w = pictures.weapons_cards[i][1]
                                c_2 = False
    return chosen_c, chosen_w
