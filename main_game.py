import random
from Board import *
from pictures import *

board = Board()
pictures = pictures()


def main():
    r_x = 16
    r_y = 0
    y_x = 23
    y_y = 7
    g_x = 9
    g_y = 24
    p_x = 0
    p_y = 5
    b_x = 0
    b_y = 18
    w_x = 14
    w_y = 24
    board.grid[r_x][r_y].sprite = pictures.red
    board.grid[y_x][y_y].sprite = pictures.yellow
    board.grid[g_x][g_y].sprite = pictures.green
    board.grid[p_x][p_y].sprite = pictures.purple
    board.grid[b_x][b_y].sprite = pictures.blue
    board.grid[w_x][w_y].sprite = pictures.white
    dagger_x = 21
    dagger_y = 1
    rope_x = 21
    rope_y = 10
    candlestick_x = 1
    candlestick_y = 1
    gun_x = 10
    gun_y = 1
    pipe_x = 1
    pipe_y = 7
    wrench_x = 1
    wrench_y = 13
    board.grid[dagger_x][dagger_y].sprite = pictures.dagger
    board.grid[rope_x][rope_y].sprite = pictures.rope
    board.grid[candlestick_x][candlestick_y].sprite = pictures.candlestick
    board.grid[gun_x][gun_y].sprite = pictures.gun
    board.grid[pipe_x][pipe_y].sprite = pictures.pipe
    board.grid[wrench_x][wrench_y].sprite = pictures.wrench

    rand_weapon = random.randint(0, 5)
    rand_suspect = random.randint(0, 5)
    rand_room = random.randint(0, 8)
    killer = (pictures.rooms_names[rand_room], pictures.suspects_names[rand_suspect], pictures.weapons_names[rand_weapon])

    players = ["r", "y", "w", "g", "b", "p"]
    running = True
    while running:
        try:
            for player in players:
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
                            if (mouse_x >= pictures.roll_button_pos[0]) and (
                                    mouse_x <= pictures.roll_button_pos[0] + 50) and \
                                    (mouse_y >= pictures.roll_button_pos[1]) and (
                                    mouse_y <= pictures.roll_button_pos[1] + 35):
                                rand = random.randint(1, 6)
                                rand2 = random.randint(1, 6)
                                draw_cube(rand, rand2)
                                pygame.display.update()
                                rand3 = rand + rand2
                                board.roll(r_x, r_y, rand3, pictures.red)
                                for i in range(board.grid_size_x):
                                    for j in range(board.grid_size_y):
                                        if board.grid[i][j].sprite is pictures.red:
                                            r_x = i
                                            r_y = j
                        """
                        if (pictures.accuse_button_pos[0] + 200 >= mouse_x >= pictures.accuse_button_pos[0]) and \
                                (pictures.accuse_button_pos[1] + 35 >= mouse_y >= pictures.accuse_button_pos[1]):
                            accuse = pygame.display.set_mode()
                        """
                draw(board)
                pygame.display.update()
        except:
            print("got shut down")
            break


if __name__ == '__main__':
    main()
