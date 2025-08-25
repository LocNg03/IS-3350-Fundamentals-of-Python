import NguyenU7AE as ma
class Dog(ma.Animal):
    def __init__(self, row, column, lives, icon, moves, demeanor, action):
        super().__init__(row, column, lives, icon, moves)
        #happy, angry
        self.demeanor = demeanor
        #sleeping, walking, barking, growling, attacking
        self.action = action

    def makePuppies(self):
        pass
