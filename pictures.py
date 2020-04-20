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

    # game pieces
    empty = pygame.image.load("game_pieces/empty.png")
    grey = pygame.image.load("game_pieces/grey_block.png")
    white_block = pygame.image.load("game_pieces/white_block.png")
    white_block = pygame.transform.scale(white_block, (80, 40))
    white_block2 = pygame.image.load("game_pieces/white_block.png")
    white_block2 = pygame.transform.scale(white_block2, (100, 40))

    # characters
    yellow = pygame.image.load("game_pieces/crl_mustard.png")
    yellow = pygame.transform.rotozoom(yellow, 0, 0.5)
    red = pygame.image.load("game_pieces/miss_scarlet.png")
    red = pygame.transform.rotozoom(red, 0, 0.5)
    green = pygame.image.load("game_pieces/mr_green.png")
    green = pygame.transform.rotozoom(green, 0, 0.5)
    purple = pygame.image.load("game_pieces/prof_plum.png")
    purple = pygame.transform.rotozoom(purple, 0, 0.5)
    white = pygame.image.load("game_pieces/mrs_white.png")
    white = pygame.transform.rotozoom(white, 0, 0.5)
    blue = pygame.image.load("game_pieces/ms_peacock.png")
    blue = pygame.transform.rotozoom(blue, 0, 0.5)

    # weapons
    dagger = pygame.image.load("game_pieces/dagger.png")
    dagger = pygame.transform.scale(dagger, (60, 30))
    rope = pygame.image.load("game_pieces/rope.png")
    rope = pygame.transform.scale(rope, (60, 30))
    wrench = pygame.image.load("game_pieces/wrench.png")
    wrench = pygame.transform.scale(wrench, (60, 30))
    pipe = pygame.image.load("game_pieces/lead_pipe.png")
    pipe = pygame.transform.scale(pipe, (60, 30))
    gun = pygame.image.load("game_pieces/gun.png")
    gun = pygame.transform.scale(gun, (60, 30))
    candlestick = pygame.image.load("game_pieces/candlestick.png")
    candlestick = pygame.transform.scale(candlestick, (60, 30))

    # board parts
    tile = pygame.image.load("game_pieces/board.jpg")
    tile = pygame.transform.rotozoom(tile, 0, 0.6)

    # doors
    # study
    study_door = pygame.image.load("game_pieces/study_door.png")
    study_door = pygame.transform.rotozoom(study_door, 0, 0.5)

    # library
    blue_library_door = pygame.image.load("game_pieces/blue_library_door.png")
    blue_library_door = pygame.transform.rotozoom(blue_library_door, 0, 0.5)
    red_library_door = pygame.image.load("game_pieces/red_library_door.png")
    red_library_door = pygame.transform.rotozoom(red_library_door, 0, 0.5)

    # billiard
    blue_billiard_door = pygame.image.load("game_pieces/blue_billiard_door.png")
    blue_billiard_door = pygame.transform.rotozoom(blue_billiard_door, 0, 0.5)
    red_billiard_door = pygame.image.load("game_pieces/red_billiard_door.png")
    red_billiard_door = pygame.transform.rotozoom(red_billiard_door, 0, 0.5)

    # conservatory
    conservatory_door = pygame.image.load("game_pieces/conservatory_door.png")
    conservatory_door = pygame.transform.rotozoom(conservatory_door, 0, 0.5)

    # hall
    blue_hall_door = pygame.image.load("game_pieces/blue_hall_door.png")
    blue_hall_door = pygame.transform.rotozoom(blue_hall_door, 0, 0.5)
    red_hall_door = pygame.image.load("game_pieces/red_hall_door.png")
    red_hall_door = pygame.transform.rotozoom(red_hall_door, 0, 0.5)
    green_hall_door = pygame.image.load("game_pieces/green_hall_door.png")
    green_hall_door = pygame.transform.rotozoom(green_hall_door, 0, 0.5)

    # ballroom
    blue_ball_door = pygame.image.load("game_pieces/blue_ball_door.png")
    blue_ball_door = pygame.transform.rotozoom(blue_ball_door, 0, 0.5)
    red_ball_door = pygame.image.load("game_pieces/red_ball_door.png")
    red_ball_door = pygame.transform.rotozoom(red_ball_door, 0, 0.5)
    green_ball_door = pygame.image.load("game_pieces/green_ball_door.png")
    green_ball_door = pygame.transform.rotozoom(green_ball_door, 0, 0.5)
    yellow_ball_door = pygame.image.load("game_pieces/yellow_ball_door.png")
    yellow_ball_door = pygame.transform.rotozoom(yellow_ball_door, 0, 0.5)

    # lounge
    lounge_door = pygame.image.load("game_pieces/lounge_door.png")
    lounge_door = pygame.transform.rotozoom(lounge_door, 0, 0.5)

    # dining room
    blue_dining_door = pygame.image.load("game_pieces/blue_dining_door.png")
    blue_dining_door = pygame.transform.rotozoom(blue_dining_door, 0, 0.5)
    red_dinning_door = pygame.image.load("game_pieces/red_dining_door.png")
    red_dinning_door = pygame.transform.rotozoom(red_dinning_door, 0, 0.5)

    # kitchen
    kitchen_door = pygame.image.load("game_pieces/kitchen_door.png")
    kitchen_door = pygame.transform.rotozoom(kitchen_door, 0, 0.5)

    # clue lists
    font = pygame.font.Font('freesansbold.ttf', 12)

    # marks
    check = pygame.image.load("green_check.png")
    check = pygame.transform.scale(check, (80, 40))
    red_x = pygame.image.load("red_x.png")
    red_x = pygame.transform.scale(red_x, (80, 40))

    # rooms
    rooms = [[List_Object(825 + i * 85, 200 + j * 45) for i in range(3)] for j in range(3)]
    rooms_names = ["study", "library", "billiard room", "conservatory", "hall", "ballroom", "lounge", "dining room",
                   "kitchen"]
    # weapons
    weapons_names = ["dagger", "lead pipe", "candlestick", "revolver", "rope", "wrench"]
    weapons = [[List_Object(1000 + i * 85, 50 + j * 45) for i in range(3)] for j in range(2)]

    # suspects
    suspects_names = ["Miss Scarlett", "Rev. Green", "Colonel Mustard", "Mrs. Peacock", "Professor Plum", "Mrs. White"]
    suspects = [[List_Object(670 + i * 105, 50 + j * 45) for i in range(3)] for j in range(2)]

    grey = pygame.transform.scale(grey, (600, 620))
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
    pygame.display.update()

    # buttons
    font2 = pygame.font.Font('freesansbold.ttf', 32)
    roll = font2.render('roll', True, Black, White)
    roll_button = roll.get_rect()
    question = font2.render('suggestion', True, Black, White)
    question_button = question.get_rect()
    accuse = font2.render('accusation', True, Black, White)
    accuse_button = question.get_rect()
    cards = font2.render('cards', True, Black, White)
    lists = font2.render('lists', True, Black, White)

    # cards
    # rooms
    ballroom_card = pygame.image.load("game_pieces/ballroom_card.png")
    ballroom_card = pygame.transform.rotozoom(ballroom_card, 0, 0.25)
    billiard_card = pygame.image.load("game_pieces/billiard_card.png")
    billiard_card = pygame.transform.rotozoom(billiard_card, 0, 0.25)
    conservatory_card = pygame.image.load("game_pieces/conservatory_card.png")
    conservatory_card = pygame.transform.rotozoom(conservatory_card, 0, 0.25)
    dining_card = pygame.image.load("game_pieces/dining_card.png")
    dining_card = pygame.transform.rotozoom(dining_card, 0, 0.25)
    hall_card = pygame.image.load("game_pieces/hall_card.png")
    hall_card = pygame.transform.rotozoom(hall_card, 0, 0.25)
    kitchen_card = pygame.image.load("game_pieces/kitchen_card.png")
    kitchen_card = pygame.transform.rotozoom(kitchen_card, 0, 0.25)
    library_card = pygame.image.load("game_pieces/library_card.png")
    library_card = pygame.transform.rotozoom(library_card, 0, 0.25)
    lounge_card = pygame.image.load("game_pieces/lounge_card.png")
    lounge_card = pygame.transform.rotozoom(lounge_card, 0, 0.25)
    study_card = pygame.image.load("game_pieces/study_card.png")
    study_card = pygame.transform.rotozoom(study_card, 0, 0.25)

    # characters
    col_mustard_card = pygame.image.load("game_pieces/col_mustard_card.png")
    col_mustard_card = pygame.transform.rotozoom(col_mustard_card, 0, 0.25)
    miss_scarlet_card = pygame.image.load("game_pieces/miss_scarlet_card.png")
    miss_scarlet_card = pygame.transform.rotozoom(miss_scarlet_card, 0, 0.25)
    mrs_peacock_card = pygame.image.load("game_pieces/mrs_peacock_card.png")
    mrs_peacock_card = pygame.transform.rotozoom(mrs_peacock_card, 0, 0.25)
    mrs_white_card = pygame.image.load("game_pieces/mrs_white_card.png")
    mrs_white_card = pygame.transform.rotozoom(mrs_white_card, 0, 0.25)
    professor_plum_card = pygame.image.load("game_pieces/professor_plum_card.png")
    professor_plum_card = pygame.transform.rotozoom(professor_plum_card, 0, 0.25)
    rev_green_card = pygame.image.load("game_pieces/rev_green_card.png")
    rev_green_card = pygame.transform.rotozoom(rev_green_card, 0, 0.25)

    # weapons
    candlestick_card = pygame.image.load("game_pieces/candlestick_card.png")
    candlestick_card = pygame.transform.rotozoom(candlestick_card, 0, 0.25)
    dagger_card = pygame.image.load("game_pieces/dagger_card.png")
    dagger_card = pygame.transform.rotozoom(dagger_card, 0, 0.25)
    gun_card = pygame.image.load("game_pieces/revolver_card.png")
    gun_card = pygame.transform.rotozoom(gun_card, 0, 0.25)
    lead_pipe_card = pygame.image.load("game_pieces/lead_pipe_card.png")
    lead_pipe_card = pygame.transform.rotozoom(lead_pipe_card, 0, 0.25)
    rope_card = pygame.image.load("game_pieces/rope_card.png")
    rope_card = pygame.transform.rotozoom(rope_card, 0, 0.25)
    wrench_card = pygame.image.load("game_pieces/wrench_card.png")
    wrench_card = pygame.transform.rotozoom(wrench_card, 0, 0.25)

    # cubes
    cube_1 = pygame.image.load("game_pieces/cube_1.png")
    cube_1 = pygame.transform.rotozoom(cube_1, 0, 0.5)
    cube_2 = pygame.image.load("game_pieces/cube_1.png")
    cube_2 = pygame.transform.rotozoom(cube_2, 0, 0.5)

    # positions
    roll_button_pos = (screensizex * 5 // 9, screensizey * 5 // 8)
    question_button_pos = (screensizex * 6 // 10 + 15, screensizey * 5 // 8)
    accuse_button_pos = (screensizex * 7 // 9 + 30, screensizey * 5 // 8)
    cards_button_pos = (screensizex * 6 // 10 + 105, screensizey * 4 // 8 + 10)
    lists_button_pos = (screensizex * 6 // 10 + 225, screensizey * 4 // 8 + 10)
    cube1_pos = (screensizex * 4 // 7 + 30, screensizey * 6 // 8 - 30)
    cube2_pos = (screensizex * 6 // 8 + 40, screensizey * 6 // 8 - 30)

    # pre game
    font3 = pygame.font.Font('freesansbold.ttf', 100)
    quest = font2.render("How many opponents do you want to play with", True, Black, White)
    oppo_amount = []
    for i in range(4):
        oppo_amount.append(List_Object(450 + 100*i, 100, font3.render(str(i+2), True, Black, White)))


def draw(board, deck, cards, ask=True):
    pictures.screen.fill(pictures.Black)
    if ask:
        pictures.screen.blit(pictures.tile, (0, 0))
    pictures.screen.blit(pictures.grey, (660, 10))
    for x in range(board.grid_size_x):
        for y in range(board.grid_size_y):
            if board.grid[x][y].sprite is not None:
                if ask:
                    pictures.screen.blit(board.grid[x][y].sprite, (board.grid[x][y].x, board.grid[x][y].y))
            if deck:
                for card in cards:
                    pictures.screen.blit(card.img, (card.x, card.y))
            else:
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
    pictures.screen.blit(pictures.roll, pictures.roll_button_pos)
    pictures.screen.blit(pictures.question, pictures.question_button_pos)
    pictures.screen.blit(pictures.accuse, pictures.accuse_button_pos)
    pictures.screen.blit(pictures.cards, pictures.cards_button_pos)
    pictures.screen.blit(pictures.lists, pictures.lists_button_pos)
    pictures.screen.blit(pictures.cube_1, pictures.cube1_pos)
    pictures.screen.blit(pictures.cube_2, pictures.cube2_pos)
    pygame.display.flip()


def draw_cube(cube1, cube2):
    pictures.cube_1 = pygame.image.load("game_pieces/cube_" + str(cube1) + ".png")
    pictures.cube_1 = pygame.transform.rotozoom(pictures.cube_1, 0, 0.5)
    pictures.cube_2 = pygame.image.load("game_pieces/cube_" + str(cube2) + ".png")
    pictures.cube_2 = pygame.transform.rotozoom(pictures.cube_2, 0, 0.5)


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
            pictures.screen.blit(characters[i], (200 + 150*i, 100))
        pictures.quest = pictures.font2.render("Waiting for opponents", True, pictures.Black, pictures.White)
        pictures.screen.blit(pictures.quest, (450, 50))
    else:
        pictures.screen.blit(pictures.quest, (300, 50))
        for i in range(4):
            pictures.screen.blit(pictures.oppo_amount[i].img, (pictures.oppo_amount[i].x, pictures.oppo_amount[i].y))
    pygame.display.flip()
