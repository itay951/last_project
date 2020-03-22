class Party:
    def __init__(self, size):
        self.size = size
        self.playres = []
        self.amount = 0

    def add(self, player):
        self.playres.append(player)
        self.amount += 1


