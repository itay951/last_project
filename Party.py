import random


class Party:
    def __init__(self, size):
        self.size = size
        self.players = []
        self.turn = 0
        self.amount = 0
        self.player_cards = [[]for i in range(self.size)]
        self.suspects = ["Miss Scarlett", "Rev. Green", "Colonel Mustard", "Mrs. Peacock", "Professor Plum", "Mrs. White"]
        self.weapons = ["dagger", "lead pipe", "candlestick", "revolver", "rope", "wrench"]
        self.rooms = ["study", "library", "billiard room", "conservatory", "hall", "ballroom", "lounge", "dining room",
                      "kitchen"]
        while len(self.suspects) > 1 or len(self.weapons) > 1 or len(self.rooms) > 1:
            for cards in self.player_cards:
                if len(self.suspects) > 1:
                    x = random.randint(0, len(self.suspects)-1)
                    cards.append(self.suspects[x])
                    self.suspects.pop(x)
                    continue
                if len(self.weapons) > 1:
                    x = random.randint(0, len(self.weapons)-1)
                    cards.append(self.weapons[x])
                    self.weapons.pop(x)
                    continue
                if len(self.rooms) > 1:
                    x = random.randint(0, len(self.rooms)-1)
                    cards.append(self.rooms[x])
                    self.rooms.pop(x)
                    continue
        self.killer = [self.suspects[0], self.weapons[0], self.rooms[0]]
        self.suspects = ["Miss Scarlett", "Rev. Green", "Colonel Mustard", "Mrs. Peacock", "Professor Plum", "Mrs. White"]
        print(self.killer)

    def add(self, player):
        self.players.append(player)
        self.amount += 1

    def full(self):
        return self.size == self.amount

    def remove(self, player):
        for i in range(len(self.players)):
            if self.players[i] is player:
                if self.full():
                    self.players[i] = "out"
                else:
                    self.suspects.append(self.player_cards[i][-1])
                    self.player_cards[i].pop(-1)
                    self.players.remove(player)
                    self.amount -= 1

    def next_turn(self):
        self.turn += 1
        if self.turn >= self.size:
            self.turn = 0

    def fileno(self):
        return self.players[0].fileno()

    def all_out(self):
        i = 0
        for player in self.players:
            if player == "out":
                i += 1
        return i+1 >= self.size
