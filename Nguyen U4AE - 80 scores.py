"""""
Program: NguyenU4AE
Author: Loc Nguyen
Last Date Modified: 02/27/2022

The purpose of this assignment enhances and applies the knowledge of chapter 4 to do input and other functions.
"""""
import statistics
print("---------------------------------------Loc's Exercise---------------------------------------") # Welcome dialogue
name = input("Enter your name: ") # Displays the string prompt and waits for keyboard input.
print("Welcome " + name, "to the new knowledge about input and output a file (.txt). ")
instruction = input("If " + name + " want to instruction how to input and output, please press (Y/N): ")
if instruction == "Y" or instruction == "yes" or instruction == "y": #The instruction is for user about how to input and output the file if they need.
    print("- First, open a text file for reading by using the open() function.")
    print("- Second, read text from the text file using the file read(), readline(), or readlines() method of the file object.")
    print("- Third, close the file using the file close() method.")
    print("- The user must be put a txt file in the same python folder that able to work.")
    print("-> For example: Users/any names/Python/ Your file.py name to open/ txt file.")
start = input("If you understand the rules, please press (c) to continues: ")
while True:
    names = input("Enter your file want here (Press x for exit): ") #The user must be put a txt file in the same python folder that able to work. 
    if names == 'x' or names == 'X':
        print('Thank you for participating, I am glad about this program has work!')
        break   
    else:
        f = open(names, 'r') #Read the file, use 'r' to read the file only.
        number = [] #An empty list. 
        for line in f: #Read the text file line by line and return all the lines as strings
            myValues = line.strip()#Use strip to remove a newline
            lines = int(myValues) #Convert str to integer 
            number.append(lines) # Add the value for the list
        f.close() 
        print("The Mean number in the file is:", statistics.mean(number)) #Calculate mean/average of a given list of numbers.
        print("The Median number in the file is:", statistics.median(number)) #Calculate median value from an unsorted data-list.
        print("The Mode number in the file is:", statistics.mode(number)) #The value that appears most often.
        print("The Standard Deviation in the file is:", statistics.stdev(number)) #Calculate the standard deviation
        print("The Variance in the file is:", statistics.variance(number)) #Measures how far the set of numbers are spread out from their average value.
        print("The Minimum in the file is:", min(number)) #Find the smallest numbers in the list.
        print("The Maximum in the file is:", max(number)) #Find the largest numbers in the list.
        ranges = max(number) - min(number)
        print("The Range in the file is:", ranges)
        print("The Sum in the file is:", sum(number)) #Calculate all numbers in the list. 
        print("The Count in the file is,", number.count(1)) #Count how many times a fixed number is displayed.
        
