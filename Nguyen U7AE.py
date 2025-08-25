"""""
Program: NguyenU9AE
Author: Loc Nguyen
Last Date Modified: 04/24/2022

demonstrate their understanding of application development, the creation and use of classes and objects in Python.
"""""
import Player as p
def main():
    print("")
    print("------------------Stray Cat Strut------------------") #Header
    print("")
    names = input("Please enter Player's Name: ")
    curPlayer = p.Player(names, 0)
    print("")
    print("Hello, " + names + ". Welcome to Stray Cat Strut!") #Welcome user
    print("---------------------------------------")
    print("")
    print("{:<17s}{:<25s}".format("Player","High Score:"))
    print("----------------------------")
    inFile = open("score.in", "r")
    for line in inFile:
        name = line.split(",")[0]
        score = line.split(",")[1]
        print("{:<16s}".format(name) + "\t" + "{:<15}".format(score))
    print("")
    ins = input("Do you need instruction " + names + "? (Y/N): ") #Instruction
    if ins == "Yes" or ins == "yes" or ins == "Y" or ins == "y":
        print("The player can move: N, E, S, W")
        print("The player can Meow(M): Makes dogs go to sleep for two turns, the cat goes from Panic to Calm.")
        print("The player can Hiss(H): Makes dogs within one grid unit back off one space, token goes from 'C' for calm to 'P' for panic, can now claw.")
        print("The player can Claw(C): Makes dogs within one grid reset at a random position, but creates another dog. The cat must have an attitude of panic to enable the claw action.")
    else:
        print("")
        print("Great, let's get started.")
    print("")
    print("Player: " + names + " Level: " + " Score: ")
    gameBoard = Grid(20, 20, " ")
    print(gameBoard)


class Grid(object):
    """Represents a 20 grid"""
    def __init__(self, rows, columns, fillValue=None):
        self.data = []
        for row in range(rows):
            dataInRow = []
            for column in range(columns):
                dataInRow.append(fillValue)
            self.data.append(dataInRow)

    def getWidth(self):
        """Return the number of columns"""
        return len(self.data[0])

    def getHeight(self):
        """Return thenumber of rows"""
        return len(self.data)

    def __str__(self):
        """Return a string representation of the 20 grid."""
        result = ""  #Initialtion the return string
        result += " " + "_"*2 * self.getWidth() + "\n"
        for row in range(self.getHeight()):
            result += "|"
            for col in range(self.getWidth()):
                result += str(self.data[row][col] + " ")
            result += "|\n"
        result += " " + "-"*2 * self.getWidth() + '\n'
        return result

    def setItem(self, row, column, value):
        """Place an item on the grid"""
        self.data[row][column] == value

    def find(self, value):
        """Return the position of an animal if found"""
        for row in range(self.getHeight()):
            for column in range(self.getWidth()):
                if self[row][column] == value:
                    return (row, column)
        return None


class Animal(object):
    def __init__(self, row, column, lives, icon, moves):
        self.currentRow = row
        self.currentCol = column
        self.location = chr(self.currentRow + 64) + str(self.currentCol)
        self.live = lives
        self.icon = icon
        self.move = moves

    def getRow(self):
        return self.currentRow

    def getCol(self):
        return self.currentCol

    def getLocation(self):
        return self.location

    def getLive(self):
        return self.live

    def getIcon(self):
        return self.icon

    def getMove(self):
        return self.move

    def left(self, event):
        self.x = -5
        self.y = 0
        print(event.keysym)

    def right(self, event):
        self.x = 5
        self.y = 0
        print(event.keysym)

    def up(self, event):
        self.x = 0
        self.y = -5
        print(event.keysym)

    def down(self, event):
        self.x = 0
        self.y = 5
        print(event.keysym)

    def __str__(self):
        result = " "
        result += "Icon:" + self.getIcon() + "\n"
        result += "Location:" + self.getLocation() + "\n"
        result += "Live:" + self.getLive() + "\n"

if __name__ == "__main__":
    main()