from pictures import *
from Board_Object import *
window_ratio = ctypes.windll.user32.GetSystemMetrics(0)/1280


class Board:
    pictures = pictures()
    grid_size_x = 24
    grid_size_y = 25
    cube_size = 24.5*window_ratio
    x_0 = 33*window_ratio
    y_0 = 30*window_ratio
    grid = []

    def __init__(self):
        self.grid = [[Board_Object(i * self.cube_size + self.x_0, j * self.cube_size + self.y_0) for j in range(self.grid_size_y)] for i in range(self.grid_size_x)]
        for i in range(self.grid_size_x):
            for j in range(self.grid_size_y):
                if (i == 0 and j != 5 and j != 18) or (j == 0 and i != 7 and i != 16) or (
                        i == 23 and j != 7 and j != 17) or \
                        (j == 24 and i != 9 and i != 14) or (j == 23 and (i == 17 or i == 6)):
                    self.grid[i][j].ident = "wall"

                # study
                if (i == 6 and 1 <= j <= 2) or(1 <= i <= 5 and j == 3):
                    self.grid[i][j].ident = "wall"
                if 1 <= i <= 5 and 1 <= j <= 2:
                    self.grid[i][j].ident = "room"
                    self.grid[i][j].room_name = "study"
                if i == 6 and j == 3:
                    self.grid[i][j].ident = "door"
                    self.grid[i][j].door_exit = "down"

                # library
                if (1 <= i <= 5 and (6 == j or j == 10)) or (i == 6 and (7 == j or j == 9)):
                    self.grid[i][j].ident = "wall"
                if 1 <= i <= 5 and 7 <= j <= 9:
                    self.grid[i][j].ident = "room"
                    self.grid[i][j].room_name = "library"
                if i == 6 and j == 8:
                    self.grid[i][j].ident = "door"
                    self.grid[i][j].door_exit = "right"
                if i == 3 and j == 10:
                    self.grid[i][j].ident = "door"
                    self.grid[i][j].door_exit = "down"

                # billiard room
                if (1 <= i <= 5 and (12 == j or j == 16)) or (i == 5 and 13 <= j <= 14):
                    self.grid[i][j].ident = "wall"
                if 13 <= j <= 15 and 1 <= i <= 4:
                    self.grid[i][j].ident = "room"
                    self.grid[i][j].room_name = "billiard room"
                if i == 1 and j == 12:
                    self.grid[i][j].ident = "door"
                    self.grid[i][j].door_exit = "up"
                if i == 5 and j == 15:
                    self.grid[i][j].ident = "door"
                    self.grid[i][j].door_exit = "right"

                # conservatory
                if (1 <= i <= 3 and 19 == j) or (i == 5 and 20 <= j <= 23):
                    self.grid[i][j].ident = "wall"
                if 1 <= i <= 4 and 20 <= j <= 22:
                    self.grid[i][j].ident = "room"
                    self.grid[i][j].room_name = "conservatory"
                if i == 4 and j == 19:
                    self.grid[i][j].ident = "door"
                    self.grid[i][j].door_exit = "right"
                if i == 4 and j == 20:
                    self.grid[i][j].sprite = pictures.empty

                # hall
                if ((9 == i or 14 == i)and 1 <= j <= 6) or (j == 6 and 9 <= i <= 14):
                    self.grid[i][j].ident = "wall"
                if 1 <= j <= 5 and 10 <= i <= 13:
                    self.grid[i][j].ident = "room"
                    self.grid[i][j].room_name = "hall"
                if (11 == i or i == 12) and j == 6:
                    self.grid[i][j].ident = "door"
                    self.grid[i][j].door_exit = "down"
                if i == 9 and j == 4:
                    self.grid[i][j].ident = "door"
                    self.grid[i][j].door_exit = "left"

                # mid board
                if 9 <= i <= 13 and 8 <= j <= 14:
                    self.grid[i][j].ident = "wall"

                # ballroom
                if (8 <= i <= 15 and (17 == j or j == 22)) or (10 <= i <= 13 and 23 == j) or (17 <= j <= 22 and (i == 8 or i == 15)):
                    self.grid[i][j].ident = "wall"
                if 9 <= i <= 14 and 18 <= j <= 21:
                    self.grid[i][j].ident = "room"
                    self.grid[i][j].room_name = "ballroom"
                if j == 17 and (i == 9 or i == 14):
                    self.grid[i][j].ident = "door"
                    self.grid[i][j].door_exit = "up"
                if j == 19 and i == 8:
                    self.grid[i][j].ident = "door"
                    self.grid[i][j].door_exit = "left"
                if i == 15 and j == 19:
                    self.grid[i][j].ident = "door"
                    self.grid[i][j].door_exit = "right"

                # lounge
                if (i == 17 and 1 <= j <= 5) or (j == 5 and 17 <= i <= 22):
                    self.grid[i][j].ident = "wall"
                if 18 <= i <= 22 and 1 <= j <= 4:
                    self.grid[i][j].ident = "room"
                    self.grid[i][j].room_name = "lounge"
                if i == 17 and j == 5:
                    self.grid[i][j].ident = "door"
                    self.grid[i][j].door_exit = "down"

                # dining room
                if (16 <= i <= 22 and 9 == j) or (19 <= i <= 22 and j == 15) or (i == 16 and 9 <= j <= 14) or (j == 14 and 16 <= i <= 18):
                    self.grid[i][j].ident = "wall"
                if 17 <= i <= 21 and 10 <= j <= 13:
                    self.grid[i][j].ident = "room"
                    self.grid[i][j].room_name = "dining room"
                if i == 17 and j == 9:
                    self.grid[i][j].ident = "door"
                    self.grid[i][j].door_exit = "up"
                if i == 16 and j == 12:
                    self.grid[i][j].ident = "door"
                    self.grid[i][j].door_exit = "left"

                # kitchen
                if (22 >= i >= 18 and 18 == j) or (23 >= j >= 18 and 18 == i):
                    self.grid[i][j].ident = "wall"
                if 19 <= i <= 22 and 19 <= j <= 23:
                    self.grid[i][j].ident = "room"
                    self.grid[i][j].room_name = "kitchen"
                if i == 19 and j == 18:
                    self.grid[i][j].ident = "door"
                    self.grid[i][j].door_exit = "up"

        for i in range(self.grid_size_x):
            for j in range(self.grid_size_y):
                if self.grid[i][j].ident == "door":
                    self.room(i+1, j, self.grid[i][j].room)
                    self.room(i-1, j, self.grid[i][j].room)
                    self.room(i, j+1, self.grid[i][j].room)
                    self.room(i, j-1, self.grid[i][j].room)
                    self.room(i-1, j-1, self.grid[i][j].room)
                    self.room(i+1, j-1, self.grid[i][j].room)

    def move(self, myself, steps, deck, cards, tu):
        # a recursive function that checks your movement input and your position and moves your your piece accordingly
        if steps != 0:
            breaked = False
            if self.grid[myself.x][myself.y].ident != "floor" or \
                    (self.grid[myself.x][myself.y].has_sprite() and self.grid[myself.x][myself.y].sprite is not myself):
                if self.grid[myself.x][myself.y].ident == "door":
                    for i in range(len(self.grid[myself.x][myself.y].room)):
                        if self.grid[myself.x][myself.y].room[i].sprite is myself.img:
                            self.grid[myself.x][myself.y].room[i].sprite = None
                            if self.grid[myself.x][myself.y].door_exit == "left":
                                self.grid[myself.x-1][myself.y].sprite = myself.img
                                myself.x = myself.x-1
                            if self.grid[myself.x][myself.y].door_exit == "right":
                                self.grid[myself.x+1][myself.y].sprite = myself.img
                                myself.x = myself.x+1
                            if self.grid[myself.x][myself.y].door_exit == "up":
                                self.grid[myself.x][myself.y-1].sprite = myself.img
                                myself.y = myself.y-1
                            if self.grid[myself.x][myself.y].door_exit == "down":
                                self.grid[myself.x][myself.y+1].sprite = myself.img
                                myself.y = myself.y+1
                            breaked = True
                            break
                    if not breaked:
                        for tile in self.grid[myself.x][myself.y].room:
                            if not tile.has_sprite():
                                self.grid[myself.x][myself.y].sprite = None
                                tile.sprite = myself.img
                                myself.x = int((tile.x - self.x_0)/self.cube_size)
                                myself.y = int((tile.y - self.y_0)/self.cube_size)
                                return
            draw(self, deck, cards, tu)
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        waiting = False
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            waiting = False
                            pygame.quit()
                        if event.key == pygame.K_LEFT:
                            if myself.x-1 >= 0:
                                if self.grid[myself.x-1][myself.y].ident != "wall":
                                    if self.grid[myself.x-1][myself.y].ident == "door":
                                        if self.grid[myself.x-1][myself.y].door_exit != "right":
                                            continue
                                    if not self.grid[myself.x-1][myself.y].has_sprite():
                                        waiting = False
                                        self.grid[myself.x][myself.y].sprite = None
                                        self.grid[myself.x-1][myself.y].sprite = myself.img
                                        draw(self, deck, cards, tu)
                                        myself.x -= 1
                                        self.move(myself, steps-1, deck, cards, tu)
                        if event.key == pygame.K_RIGHT:
                            if myself.x+1 <= 23:
                                if self.grid[myself.x+1][myself.y].ident != "wall":
                                    if self.grid[myself.x+1][myself.y].ident == "door":
                                        if self.grid[myself.x+1][myself.y].door_exit != "left":
                                            continue
                                    if not self.grid[myself.x+1][myself.y].has_sprite():
                                        waiting = False
                                        self.grid[myself.x][myself.y].sprite = None
                                        self.grid[myself.x+1][myself.y].sprite = myself.img
                                        draw(self, deck, cards, tu)
                                        myself.x += 1
                                        self.move(myself, steps-1, deck, cards, tu)
                        if event.key == pygame.K_UP:
                            if myself.y-1 >= 0:
                                if self.grid[myself.x][myself.y-1].ident != "wall":
                                    if self.grid[myself.x][myself.y-1].ident == "door":
                                        if self.grid[myself.x][myself.y-1].door_exit != "down":
                                            continue
                                    if not self.grid[myself.x][myself.y-1].has_sprite():
                                        waiting = False
                                        self.grid[myself.x][myself.y].sprite = None
                                        self.grid[myself.x][myself.y-1].sprite = myself.img
                                        draw(self, deck, cards, tu)
                                        myself.y -= 1
                                        self.move(myself, steps-1, deck, cards, tu)
                        if event.key == pygame.K_DOWN:
                            if myself.y+1 <= 24:
                                if self.grid[myself.x][myself.y+1].ident != "wall":
                                    if self.grid[myself.x][myself.y+1].ident == "door":
                                        if self.grid[myself.x][myself.y+1].door_exit != "up":
                                            continue
                                    if not self.grid[myself.x][myself.y+1].has_sprite():
                                        waiting = False
                                        self.grid[myself.x][myself.y].sprite = None
                                        self.grid[myself.x][myself.y+1].sprite = myself.img
                                        draw(self, deck, cards, tu)
                                        myself.y += 1
                                        self.move(myself, steps-1,  deck, cards, tu)

        if self.grid[myself.x][myself.y].ident != "floor" or \
                (self.grid[myself.x][myself.y].has_sprite() and self.grid[myself.x][myself.y].sprite is not myself.img):
            if self.grid[myself.x][myself.y].ident == "door":
                for tile in self.grid[myself.x][myself.y].room:
                    if not tile.has_sprite():
                        self.grid[myself.x][myself.y].sprite = None
                        tile.sprite = myself.img
                        myself.x = int((tile.x - self.x_0)/self.cube_size)
                        myself.y = int((tile.y - self.y_0)/self.cube_size)
                        return

    def roll(self, me, rand, deck, cards, tur):
        # checks if the player in a room and let him to get out and then call move
        if self.grid[me.x][me.y].ident == "room":
            x1, y1, x2, y2, x3, y3, x4, y4 = self.find_door(me.x, me.y)

            not_pressed = True
            while not_pressed:
                draw(self, deck, cards, tur)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            return True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            me.x = x1
                            me.y = y1
                            not_pressed = False
                        if event.key == pygame.K_2:
                            if x2 != 0:
                                me.x = x2
                                me.y = y2
                                not_pressed = False
                        if event.key == pygame.K_3:
                            if x3 != 0:
                                me.x = x3
                                me.y = y3
                                not_pressed = False
                        if event.key == pygame.K_4:
                            if x4 != 0:
                                me.x = x4
                                me.y = y4
                                not_pressed = False

            self.grid[x1][y1].sprite = None
            self.grid[x2][y2].sprite = None
            self.grid[x3][y3].sprite = None
            self.grid[x4][y4].sprite = None

        self.move(me, rand, deck, cards, tur)

    def room(self, x, y, arr):
        # make an array of all the room parts that connect to a specific door
        for i in range(len(arr)):
            if arr[i] is self.grid[x][y]:
                return
        if self.grid[x][y].ident == "room":
            arr.append(self.grid[x][y])
            self.room(x+1, y, arr)
            self.room(x-1, y, arr)
            self.room(x, y+1, arr)
            self.room(x, y-1, arr)

    def find_door(self, x, y):
        # return the doors that are connected to each room
        x1 = 0
        y1 = 0
        x2 = 0
        y2 = 0
        x3 = 0
        y3 = 0
        x4 = 0
        y4 = 0
        if self.grid[x][y].room_name == "study":
            x1 = 6
            y1 = 3
            self.grid[x1][y1].sprite = pictures.study_door
        if self.grid[x][y].room_name == "library":
            x1 = 6
            y1 = 8
            self.grid[x1][y1].sprite = pictures.blue_library_door
            x2 = 3
            y2 = 10
            self.grid[x2][y2].sprite = pictures.red_library_door
        if self.grid[x][y].room_name == "billiard room":
            x1 = 1
            y1 = 12
            self.grid[x1][y1].sprite = pictures.blue_billiard_door
            x2 = 5
            y2 = 15
            self.grid[x2][y2].sprite = pictures.red_billiard_door
        if self.grid[x][y].room_name == "conservatory":
            x1 = 4
            y1 = 19
            self.grid[x1][y1].sprite = pictures.conservatory_door
        if self.grid[x][y].room_name == "hall":
            x1 = 11
            y1 = 6
            self.grid[x1][y1].sprite = pictures.blue_hall_door
            x2 = 12
            y2 = 6
            self.grid[x2][y2].sprite = pictures.red_hall_door
            x3 = 9
            y3 = 4
            self.grid[x3][y3].sprite = pictures.green_hall_door
        if self.grid[x][y].room_name == "ballroom":
            x1 = 9
            y1 = 17
            self.grid[x1][y1].sprite = pictures.blue_ball_door
            x2 = 14
            y2 = 17
            self.grid[x2][y2].sprite = pictures.red_ball_door
            x3 = 8
            y3 = 19
            self.grid[x3][y3].sprite = pictures.green_ball_door
            x4 = 15
            y4 = 19
            self.grid[x4][y4].sprite = pictures.yellow_ball_door
        if self.grid[x][y].room_name == "lounge":
            x1 = 17
            y1 = 5
            self.grid[x1][y1].sprite = pictures.lounge_door
        if self.grid[x][y].room_name == "dining room":
            x1 = 17
            y1 = 9
            self.grid[x1][y1].sprite = pictures.blue_dining_door
            x2 = 16
            y2 = 12
            self.grid[x2][y2].sprite = pictures.red_dinning_door
        if self.grid[x][y].room_name == "kitchen":
            x1 = 19
            y1 = 18
            self.grid[x1][y1].sprite = pictures.kitchen_door

        return x1, y1, x2, y2, x3, y3, x4, y4
