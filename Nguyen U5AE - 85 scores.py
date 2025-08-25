"""""
Program: NguyenU5AE
Author: Loc Nguyen
Last Date Modified: 03/20/2022

This assignment uses list and dictionaries for create the roll dice game.
"""""

import random
import statistics
print("")
print("--------------------------------------------Roll Dice game--------------------------------------------")
print("")

"""Introduce the rule of the roll dice game"""
name = input("Enter your name here: ")
print("Welcome " + name, "to roll dice game play. I hope you will have a fun time.")
print("")
print("                                                NOTICE:                                               ")
print("- In this game, we use six-sided dice for rolling dice and can choose more than one dice in this game.")
print("- At the end of each roll of the dice, there will be:")
print("  + A notice of the percentage of numbers that have been displayed.")
print("  + The Descriptive statistics reports")
print("- If you are already to play.")
start = input("-> Please press (Y) to start the game: ")
while True:
    if start == "y" or start == " Yes" or start == "Y" or start == "yes":
        print("")
        
        """List the number results of the roll dice game"""
        dices = int(input("How many dice do you want to use?: "))
        times = int(input("How many times do you want to roll dice?: "))
        roll = [random.randint(1, 6) for i in range(times)] # This displays for one dice with six sides, including 1 to 6.
        if dices >= 2:  # In this code line for a situation, players choose one more dice.
            roll = [random.randint(1*dices, 6*dices) for i in range(times)] # Each side will be multiplied by the equivalent of the player's dice chosen.
        print("The Dice Roll is: ", roll)
        print("")
        print("Thank for you using! Enjoy")
        print("")

        """Start convert to the visualization table"""
        print("------------------------------------------------------------------------------------------------------")
        print("{""}{:>11}{:>12}{:>12}".format('#','Count','Percentage','Graph'))  # The header of table
        print("------------------------------------------------------------------------------------------------------")

        def countX(roll, x): #Count numbers are displayed in the roll dice game.
            return roll.count(x)
        for i in range(dices, dices*6+1): # Return the percentage values of each number displayed in the roll dice game.
            d = (countX(roll, i)*100/times)
            print('{:>4}{:>7}'.format(i, countX(roll, i)),
                  '{:>11}'.format('{:0.2f}%'.format(d)), 
                  '{:>2}'.format(''),
                  '{:<15}'.format('|' * int(d+1)))
        print("------------------------------------------------------------------------------------------------------")
        print("Sum:", f'{times:>6}{("100%"):>12}')
        print("")
        print("")

        "Descriptive statistics report"
        print("------------------------------------------------------------------------------------------------------")
        print("                          The Descriptive statistics report is shown below:                           ")
        print("")
        number = []
        for line in roll:  # Read the text file line by line and return all the lines as strings
            lines = int(line)  # Convert str to integer
            number.append(lines)  # Adding the value for the list
        print("The Mean number in the file is:", statistics.mean(number))
        print("The Median number in the file is:", statistics.median(number))
        print("The Mode number in the file is:", statistics.mode(number))
        print("The Standard Deviation in the file is:", statistics.stdev(number))
        print("The Variance in the file is:", statistics.variance(number))
        print("The Minimum in the file is:", min(number))
        print("The Maximum in the file is:", max(number))
        print("The Range in the file is:", max(number)-min(number))
        print("The Sum in the file is:", sum(number))
        print("The Count number 10 in the file is:", number.count(10))
        print("------------------------------------------------------------------------------------------------------")
        print("")
        print("                 Thank you for participating, I am glad about this program has work!                  ")
        print("")
        print("------------------------------------------------------------------------------------------------------")
        print("")
        agains = input("Do you want try again(Y/N)?: ")
        if agains == "N" or agains == "n" or agains == "No" or agains == "no":
            print("")
            print("                              Thank for your using the program! ")
            print("")
            break   
    else:
        print("")
        print("Please try the program again!")
        print("")
        print("")
        break
         
        