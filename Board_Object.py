class Board_Object:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ident = "floor"
        self.sprite = None
        self.room = []
        self.door_exit = ""
        self.optional_door = None
        self.room_name = ""
        self.weapon_place = ()

    def has_sprite(self):
        return self.sprite is not None


