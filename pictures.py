import pygame
import ctypes
import os
from Board_Object import *
pygame.init()
user32 = ctypes.windll.user32
screensizex = user32.GetSystemMetrics(0)
screensizey = user32.GetSystemMetrics(1)
place_win = (0, 30)
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % place_win


class pictures:
    # colors

    Black = (0, 0, 0)
    Grey = (211, 211, 211)
    White = (255, 255, 255)
    # screen

    screen = pygame.display.set_mode((screensizex, screensizey), pygame.RESIZABLE)
    pygame.display.set_caption("cluedo")
    # game pieces
    empty = pygame.image.load("game_pieces/empty.png")
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
    screen.fill(Black)
    # clue lists
    # marks
    check = pygame.image.load("green_check.png")
    check = pygame.transform.scale(check, (80, 40))
    red_x = pygame.image.load("red_x.png")
    red_x = pygame.transform.scale(red_x, (80, 40))
    # rooms
    rooms_names = ["study", "library", "billiard room", "conservatory", "hall", "ballroom", "lounge", "dining room", "kitchen"]
    font = pygame.font.Font('freesansbold.ttf', 12)
    pygame.draw.rect(screen, Grey, (660, 10, 600, 620))
    rooms = [[Board_Object(825 + i*85, 200 + j*45)for i in range(3)]for j in range(3)]
    k = 0
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(screen, White, (rooms[i][j].x, rooms[i][j].y, 80, 40))
            screen.blit(font.render(rooms_names[k], True, Black, White), (rooms[i][j].x, rooms[i][j].y+15))
            k += 1
    # weapons
    weapons_names = ["dagger", "lead pipe", "candlestick", "revolver", "rope", "wrench"]
    font = pygame.font.Font('freesansbold.ttf', 12)
    weapons = [[Board_Object(1000 + i * 85, 50 + j * 45) for i in range(3)] for j in range(2)]
    k = 0
    for i in range(2):
        for j in range(3):
            pygame.draw.rect(screen, White, (weapons[i][j].x, weapons[i][j].y, 80, 40))
            screen.blit(font.render(weapons_names[k], True, Black, White), (weapons[i][j].x, weapons[i][j].y + 15))
            k += 1
    # suspects
    suspects_names = ["Miss Scarlett", "Mr. Green", "Colonel Mustard", "Mrs. Peacock", "Prof. Plum", "Mrs. White"]
    font = pygame.font.Font('freesansbold.ttf', 12)
    suspects = [[Board_Object(670 + i * 105, 50 + j * 45) for i in range(3)] for j in range(2)]
    k = 0
    for i in range(2):
        for j in range(3):
            pygame.draw.rect(screen, White, (suspects[i][j].x, suspects[i][j].y, 100, 40))
            screen.blit(font.render(suspects_names[k], True, Black, White), (suspects[i][j].x, suspects[i][j].y + 15))
            k += 1

    # buttons

    font = pygame.font.Font('freesansbold.ttf', 32)
    roll = font.render('roll', True, Black, White)
    roll_button = roll.get_rect()
    question = font.render('questioning', True, Black, White)
    question_button = question.get_rect()
    accuse = font.render('accusation', True, Black, White)
    accuse_button = question.get_rect()
    # positions

    roll_button_pos = (screensizex * 5 // 9, screensizey * 5 // 8)
    question_button_pos = (screensizex * 6 // 10 + 15, screensizey * 5 // 8)
    accuse_button_pos = (screensizex * 7 // 9 + 30, screensizey * 5 // 8)
    cube1_pos = (screensizex * 4 // 7 + 30, screensizey * 6 // 8 - 30)
    cube2_pos = (screensizex * 6 // 8 + 40, screensizey * 6 // 8 - 30)

    # cubes
    cube = pygame.image.load("game_pieces/cube_1.png")
    cube = pygame.transform.rotozoom(cube, 0, 0.5)
    screen.blit(cube, cube1_pos)
    screen.blit(cube, cube2_pos)


def draw(board):
    pictures.screen.blit(pictures.tile, (0, 0))
    for x in range(board.grid_size_x):
        for y in range(board.grid_size_y):
            if board.grid[x][y].sprite is not None:
                pictures.screen.blit(board.grid[x][y].sprite, (board.grid[x][y].x, board.grid[x][y].y))
            try:
                if pictures.rooms[x][y].sprite is not None:
                    pictures.screen.blit(pictures.rooms[x][y].sprite, (pictures.rooms[x][y].x, pictures.rooms[x][y].y))
                if pictures.suspects[x][y].sprite is not None:
                    pictures.screen.blit(pictures.suspects[x][y].sprite, (pictures.suspects[x][y].x, pictures.suspects[x][y].y))
                if pictures.weapons[x][y].sprite is not None:
                    pictures.screen.blit(pictures.weapons[x][y].sprite, (pictures.weapons[x][y].x, pictures.weapons[x][y].y))
            except:
                pass
    pictures.screen.blit(pictures.roll, pictures.roll_button_pos)
    pictures.screen.blit(pictures.question, pictures.question_button_pos)
    pictures.screen.blit(pictures.accuse, pictures.accuse_button_pos)
    pygame.display.flip()


def draw_cube(cube1, cube2):
    cube = pygame.image.load("game_pieces/cube_" + str(cube1) + ".png")
    cube = pygame.transform.rotozoom(cube, 0, 0.5)
    pictures.screen.blit(cube, pictures.cube1_pos)
    cube = pygame.image.load("game_pieces/cube_" + str(cube2) + ".png")
    cube = pygame.transform.rotozoom(cube, 0, 0.5)
    pictures.screen.blit(cube, pictures.cube2_pos)
