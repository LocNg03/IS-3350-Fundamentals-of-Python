import NguyenU7AE as ma
class Cat(ma.Animal):
    def __init__(self, row, column, lives, icon, moves, attitude, response):
        super().__init__(row, column, lives, icon, moves)
        # Calm, Strut, Panic
        self.attitude = attitude
        # Meow, Hiss, Claw
        self.response = response

    def loseLife(self):
        self.live -= 1

    def meow(self):
        #
        print("Meow")

    def hiss(self):
        #
        print("Hiss")

    def claw(self):
        #
        print("Claw")
