class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return str(self.name) + " " + str(self.score)
