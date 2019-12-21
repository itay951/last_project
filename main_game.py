import pygame
import ctypes
import random
import os
user32 = ctypes.windll.user32
screensizex = user32.GetSystemMetrics(0)
screensizey = user32.GetSystemMetrics(1)
pygame.init()
x_0 = 33
y_0 = 30
movement_speed = 24.5
x_len = 24
y_len = 25
board = [[[(i*movement_speed + x_0, j*movement_speed + y_0), None] for j in range(y_len)] for i in range(x_len)]
for i in range(x_len):
    for j in range(y_len):
        if (i == 0 and j != 5 and j != 18) or (j == 0 and i != 7 and i != 16) or (i == 23 and j != 7 and j != 17) or \
                (j == 24 and i != 9 and i != 14) or (j == 23 and (i == 17 or i == 6)):
                board[i][j][0] = (0, 0)
        # study
        if 1 <= i <= 6 and 1 <= j <= 3:
            board[i][j][0] = (0, 0)
        # library
        if (1 <= i <= 5 and 6 <= j <= 10) or (i == 6 and 7 <= j <= 9):
            board[i][j][0] = (0, 0)
        # billiard room
        if 1 <= i <= 5 and 12 <= j <= 16:
            board[i][j][0] = (0, 0)
        # conservatory
        if(1 <= i <= 4 and 19 <= j <= 23) or (i == 5 and 20 <= j <= 23):
            board[i][j][0] = (0, 0)
        # hall
        if 9 <= i <= 14 and 1 <= j <= 6:
            board[i][j][0] = (0, 0)
        # mid board
        if 9 <= i <= 13 and 8 <= j <= 14:
            board[i][j][0] = (0, 0)
        # ballroom
        if (8 <= i <= 15 and 17 <= j <= 22) or (10 <= i <= 13 and 23 <= j <= 24):
            board[i][j][0] = (0, 0)
        # lounge
        if 17 <= i <= 22 and 1 <= j <= 5:
            board[i][j][0] = (0, 0)
        # dining room
        if (16 <= i <= 22 and 9 <= j <= 14) or (19 <= i <= 22 and j == 15):
            board[i][j][0] = (0, 0)
        # kitchen
        if 18 <= i <= 22 and 18 <= j <= 23:
            board[i][j][0] = (0, 0)

place_win = (0, 30)
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % place_win
screen = pygame.display.set_mode((screensizex, screensizey), pygame.RESIZABLE)
pygame.display.set_caption("cluedo")
choose = pygame.image.load("choseable_tile.png").convert_alpha()
choose = pygame.transform.rotozoom(choose, 0, 0.6)
red = pygame.image.load("game_pieces/miss_scarlet.png")
red = pygame.transform.rotozoom(red, 0, 0.5)
tile = pygame.image.load("board.jpg")
tile = pygame.transform.rotozoom(tile, 0, 0.6)
screen.fill((0, 0, 0))
pygame.display.flip()


def move_options(x, y, steps, grid):
    global choose
    if steps != 0:
        if grid[x][y][0] == (0, 0):
            return
        if not y == 0:
            move_options(x, y-1, steps-1, grid)
        if not y == 24:
            move_options(x, y+1, steps-1, grid)
        if not x == 23:
            move_options(x+1, y, steps-1, grid)
        if not x == 0:
            move_options(x-1, y, steps-1, grid)
        board[x][y][1] = choose


def turn(tiles, posx, posy):
    rand = random.randint(2, 12)
    if not posy == 0:
        move_options(posx, posy - 1, rand, tiles)
    if not posx == 0:
        move_options(posx - 1, posy, rand, tiles)
    if not posy == 24:
        move_options(posx, posy + 1, rand, tiles)
    if not posx == 23:
        move_options(posx + 1, posy, rand, tiles)


def draw():
    global x_len, y_len, screen, board, tile, x_0
    screen.fill((0, 0, 0))
    screen.blit(tile, (0, 0))
    for x in range(x_len):
        for y in range(y_len):
            if board[x][y][1] is not None:
                screen.blit(board[x][y][1], board[x][y][0])


def main():
    global red, screen, tile, board, choose
    r_x = 16
    r_y = 0
    board[r_x][r_y][1] = red
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_1:
                    turn(board, r_x, r_y)
                    board[r_x][r_y][1] = red
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x_m, y_m = event.pos
                    x_m = int((x_m - x_0) // movement_speed)
                    y_m = int((y_m - y_0) // movement_speed)
                    if board[x_m][y_m][1] is not None:
                        r_x = x_m
                        r_y = y_m
                        for i in range(x_len):
                            for j in range(y_len):
                                board[i][j][1] = None
                        board[r_x][r_y][1] = red

        draw()
        pygame.display.update()


if __name__ == '__main__':
    main()
