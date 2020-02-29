from Board_Object import *
from pictures import *


class Board:
    pictures = pictures()
    grid_size_x = 24
    grid_size_y = 25
    cube_size = 24.5
    x_0 = 33
    y_0 = 30
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
                    self.grid[i][j].optional_door = pictures.blue_study_door

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
                    self.grid[i][j].room_name = "billiard"
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
                    self.grid[i][j].room_name = "dining"
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

    def move(self, posx, posy, steps, myself):
        if steps != 0:
            breaked = False
            if self.grid[posx][posy].ident != "floor" or \
                    (self.grid[posx][posy].has_sprite() and self.grid[posx][posy].sprite is not myself):
                if self.grid[posx][posy].ident == "door":
                    self.grid[posx][posy].sprite = None
                    for i in range(len(self.grid[posx][posy].room)):
                        if self.grid[posx][posy].room[i].sprite is myself:
                            self.grid[posx][posy].room[i].sprite = None
                            if self.grid[posx][posy].door_exit == "left":
                                self.grid[posx-1][posy].sprite = myself
                                posx = posx-1
                            if self.grid[posx][posy].door_exit == "right":
                                self.grid[posx+1][posy].sprite = myself
                                posx = posx+1
                            if self.grid[posx][posy].door_exit == "up":
                                self.grid[posx][posy-1].sprite = myself
                                posy = posy-1
                            if self.grid[posx][posy].door_exit == "down":
                                self.grid[posx][posy+1].sprite = myself
                                posy = posy+1
                            breaked = True
                            break
                    if not breaked:
                        for i in range(len(self.grid[posx][posy].room)):
                            if not self.grid[posx][posy].room[i].has_sprite():
                                self.grid[posx][posy].room[i].sprite = myself
                                return
            draw(self)
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
                            if posx-1 >= 0:
                                if self.grid[posx-1][posy].ident != "wall":
                                    if self.grid[posx-1][posy].ident == "door":
                                        if self.grid[posx-1][posy].door_exit != "right":
                                            break
                                    waiting = False
                                    self.grid[posx][posy].sprite = None
                                    self.grid[posx-1][posy].sprite = myself
                                    draw(self)
                                    self.move(posx-1, posy, steps-1, myself)
                        if event.key == pygame.K_RIGHT:
                            if posx+1 <= 23:
                                if self.grid[posx+1][posy].ident != "wall":
                                    if self.grid[posx+1][posy].ident == "door":
                                        if self.grid[posx+1][posy].door_exit != "left":
                                            break
                                    waiting = False
                                    self.grid[posx][posy].sprite = None
                                    self.grid[posx+1][posy].sprite = myself
                                    draw(self)
                                    self.move(posx+1, posy, steps-1, myself)
                        if event.key == pygame.K_UP:
                            if posy-1 >= 0:
                                if self.grid[posx][posy-1].ident != "wall":
                                    if self.grid[posx][posy-1].ident == "door":
                                        if self.grid[posx][posy-1].door_exit != "down":
                                            break
                                    waiting = False
                                    self.grid[posx][posy].sprite = None
                                    self.grid[posx][posy-1].sprite = myself
                                    draw(self)
                                    self.move(posx, posy-1, steps-1, myself)
                        if event.key == pygame.K_DOWN:
                            if posy+1 <= 24:
                                if self.grid[posx][posy+1].ident != "wall":
                                    if self.grid[posx][posy+1].ident == "door":
                                        if self.grid[posx][posy+1].door_exit != "up":
                                            break
                                    waiting = False
                                    self.grid[posx][posy].sprite = None
                                    self.grid[posx][posy+1].sprite = myself
                                    draw(self)
                                    self.move(posx, posy+1, steps-1, myself)
            if steps == 0:
                self.grid[posx][posy].sprite = myself

        if self.grid[posx][posy].ident != "floor" or \
                (self.grid[posx][posy].has_sprite() and self.grid[posx][posy].sprite is not myself):
            if self.grid[posx][posy].ident == "door":
                for i in range(len(self.grid[posx][posy].room)):
                    if not self.grid[posx][posy].room[i].has_sprite():
                        self.grid[posx][posy].room[i].sprite = myself
                        return

    def roll(self, x, y, rand, me):
        if self.grid[x][y].ident == "room":
            x1, y1, x2, y2, x3, y3, x4, y4 = self.find_door(x, y)

            not_pressed = True
            while not_pressed:
                draw(self)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            x = x1
                            y = y1
                            not_pressed = False
                        if event.key == pygame.K_2:
                            if x2 != 0:
                                x = x2
                                y = y2
                                not_pressed = False
                        if event.key == pygame.K_3:
                            if x3 != 0:
                                x = x3
                                y = y3
                                not_pressed = False
                        if event.key == pygame.K_4:
                            if x4 != 0:
                                x = x4
                                y = y4
                                not_pressed = False

        self.move(x, y, rand, me)

    def room(self, x, y, arr):
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
            self.grid[x1][y1].sprite = self.grid[x][y].optional_door
        if self.grid[x][y].room_name == "library":
            x1 = 6
            y1 = 8
            x2 = 3
            y2 = 10
        if self.grid[x][y].room_name == "billiard":
            x1 = 1
            y1 = 12
            x2 = 5
            y2 = 15
        if self.grid[x][y].room_name == "conservatory":
            x1 = 4
            y1 = 19
        if self.grid[x][y].room_name == "hall":
            x1 = 11
            y1 = 6
            x2 = 12
            y2 = 6
            x3 = 9
            y3 = 4
        if self.grid[x][y].room_name == "ballroom":
            x1 = 9
            y1 = 17
            x2 = 14
            y2 = 17
            x3 = 8
            y3 = 19
            x4 = 15
            y4 = 19
        if self.grid[x][y].room_name == "lounge":
            x1 = 17
            y1 = 5
        if self.grid[x][y].room_name == "dining":
            x1 = 17
            y1 = 9
            x2 = 16
            y2 = 12
        if self.grid[x][y].room_name == "kitchen":
            x1 = 19
            y1 = 18
        return x1, y1, x2, y2, x3, y3, x4, y4
