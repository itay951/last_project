import random
from Board import *
from pictures import *
from Sprite import *
import socket


board = Board()
pictures = pictures()
red = Sprite("red", 16, 0, pictures.red)
yellow = Sprite("yellow", 23, 7, pictures.yellow)
green = Sprite("green", 9, 24, pictures.green)
purple = Sprite("purple", 0, 5, pictures.purple)
blue = Sprite("blue", 0, 18, pictures.blue)
white = Sprite("white", 14, 24, pictures.white)
dagger = Sprite("dagger", 21, 1, pictures.dagger)
rope = Sprite("rope", 21, 10, pictures.rope)
candlestick = Sprite("candlestick", 1, 1, pictures.candlestick)
gun = Sprite("gun", 10, 1, pictures.gun)
pipe = Sprite("pipe", 1, 7, pictures.pipe)
wrench = Sprite("wrench", 1, 13, pictures.wrench)


def ask():
    pass


def accuse():
    pass


def show_cards():
    pass


def update():
    board.grid[red.x][red.y].sprite = red.img
    board.grid[yellow.x][yellow.y].sprite = yellow.img
    board.grid[green.x][green.y].sprite = green.img
    board.grid[purple.x][purple.y].sprite = purple.img
    board.grid[blue.x][blue.y].sprite = blue.img
    board.grid[white.x][white.y].sprite = white.img
    board.grid[dagger.x][dagger.y].sprite = dagger.img
    board.grid[rope.x][rope.y].sprite = rope.img
    board.grid[candlestick.x][candlestick.y].sprite = candlestick.img
    board.grid[gun.x][gun.y].sprite = gun.img
    board.grid[pipe.x][pipe.y].sprite = pipe.img
    board.grid[wrench.x][wrench.y].sprite = wrench.img


def move():
    rand = random.randint(1, 6)
    rand2 = random.randint(1, 6)
    draw_cube(rand, rand2)
    pygame.display.update()
    rand3 = rand + rand2
    returned = board.roll(red.x, red.y, rand3, red.img)
    if returned:
        return False
    for i in range(board.grid_size_x):
        for j in range(board.grid_size_y):
            if board.grid[i][j].sprite is red.img:
                red.x = i
                red.y = j
    return True


def main():
    running = True
    while running:
        update()
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    print(event.pos)
                    for i in range(3):
                        for j in range(3):
                            if pictures.rooms[i][j].x <= mouse_x <= pictures.rooms[i][j].x + 80 and \
                                    pictures.rooms[i][j].y <= mouse_y <= pictures.rooms[i][j].y + 40:
                                if event.button == 1:
                                    pictures.rooms[i][j].sprite = pictures.check
                                if event.button == 3:
                                    pictures.rooms[i][j].sprite = pictures.red_x
                            try:
                                if pictures.weapons[i][j].x <= mouse_x <= pictures.weapons[i][j].x + 80 and \
                                        pictures.weapons[i][j].y <= mouse_y <= pictures.weapons[i][j].y + 40:
                                    if event.button == 1:
                                        pictures.weapons[i][j].sprite = pictures.check
                                    if event.button == 3:
                                        pictures.weapons[i][j].sprite = pictures.red_x
                                if pictures.suspects[i][j].x <= mouse_x <= pictures.suspects[i][j].x + 100 and \
                                        pictures.suspects[i][j].y <= mouse_y <= pictures.suspects[i][j].y + 40:
                                    if event.button == 1:
                                        check = pygame.transform.scale(pictures.check, (100, 40))
                                        pictures.suspects[i][j].sprite = check
                                    if event.button == 3:
                                        red_x = pygame.transform.scale(pictures.red_x, (100, 40))
                                        pictures.suspects[i][j].sprite = red_x
                            except:
                                pass
                            draw(board)
                    if event.button == 1:
                        if (pictures.roll_button_pos[0] <= mouse_x <= pictures.roll_button_pos[0] + 50) and \
                                (pictures.roll_button_pos[1] <= mouse_y <= pictures.roll_button_pos[1] + 35):
                            running = move()
                        if (pictures.cards_button_pos[0] <= mouse_x <= pictures.cards_button_pos[0] + 100) and \
                                (pictures.cards_button_pos[1] <= mouse_y <= pictures.cards_button_pos[1] + 35):
                            show_cards()
                        if (pictures.accuse_button_pos[0] + 200 >= mouse_x >= pictures.accuse_button_pos[0]) and \
                                (pictures.accuse_button_pos[1] + 35 >= mouse_y >= pictures.accuse_button_pos[1]):
                            accuse()
                        if (pictures.question_button_pos[0] + 200 >= mouse_x >= pictures.question_button_pos[0]) and \
                                (pictures.question_button_pos[1] + 35 >= mouse_y >= pictures.question_button_pos[1]):
                            ask()
            draw(board)
            pygame.display.update()
        except:
            print("got shut down")
            break


if __name__ == '__main__':
    main()
