"""""
Program: NguyenU6AE
Author: Loc Nguyen
Last Date Modified: 02/27/2022

The purpose of this assignment creates the functions for descriptive statistics reports and others.
"""""

import statistics
import math
def main():
    'Welcome users'
    print('')
    names = input('Please provide the name you would like to use for this session: ')
    print('')
    print('Hello,', names + '.','Welcome to the Descriptive Statistics Application (DSA).') # Welcome dialogue
    print('')
    instruction = input("Do you need instruction " + names + '? (Y/N): ')
    print('')
    if instruction == "Y" or instruction == "yes" or instruction == "y" or instruction == 'Yes': # The instruction is for user about how to input and output the file if they need.
        print("- First, open a text file for reading by using the open() function.")
        print("- Second, read text from the text file using the file read(), readline(), or readlines() method of the file object.")
        print("- Third, close the file using the file close() method.")
        print("- The user must be put a txt file in the same python folder that able to work.")
        print("-> For example: Users/any names/Python/ txt file.")
    else:
        print('')
        print("Great, let's get started.")
    print('')
    while True:
        "Open file"
        file_names = input("Would you like to analyze a data file?: (y/n) ")
        if file_names == 'y' or file_names == 'Yes' or file_names == 'yes' or file_names == 'Y':
            print('')
            file_name = input('Please enter the name of the file: ') # The user must be put a txt file in the same python folder that able to work.
            print(names + ' entered ' + file_name)
            print('')
            print("File " + file_name + ' found in the current working directory.')
            print('')
            print(names, 'please see the Descriptive Statistics for the values in the' + file_name + ' file listed in the table below:')
            print('')
            open_file = open(file_name, 'r') # Read the file, use 'r' to read the file only.
            numbers = []  # An empty list.
            for line in open_file:  # Read the text file line by line and return all the lines as strings
                myValues = line.strip()  # Use strip to remove a newline
                lines = int(myValues)  # Convert str to integer
                numbers.append(lines)  # Add the value for the list
            open_file.close()
            
            "Descriptive statistics report"
            def myMean(numberz): # Calculate mean/average of a given list of numbers.
                a = len(numberz)
                b = sum(numberz)
                return b/a
            def myMedian(numberz): # Calculate median value from an unsorted data-list.
                n = len(numberz)
                index = n // 2 
                # Sample with an odd number of observations
                if n % 2:
                    return sorted(numberz)[index]
                # Sample with an even number of observations
                return sum(sorted(numberz)[index - 1:index + 1]) / 2
            def myMode(numberz): # The value that appears most often.
                c = max(set(numberz), key = numberz.count)  
                return c
            def mySt(numberz): # Calculate the standard deviation
                d = myVa(numberz)
                std = math.sqrt(d)
                return std
            def myVa(numberz): # Measures how far the set of numbers are spread out from their average value.
                n = len(numberz)
                means = sum(numberz) / n
                deviations = [(x-means)**2 for x in numberz]
                variances = sum(deviations) / n  
                return variances
            def myMi(numberz): # Find the smallest numbers in the list.
                f = min(numberz)  
                return f
            def myMa(numberz): # Find the largest numbers in the list.
                g = max(numberz)  
                return g
            def myRa(numberz):
                h = max(numberz) - min(numberz) 
                return h 
            def mySu(numberz): # Calculate all numbers in the list. 
                total = 0
                for m in numberz:
                    total += m
                return total
            def myCo(numberz): #Count how many times all number is displayed.
                count = 0
                for l in numberz:
                    count += 1
                return count
            print('{}{:>30}'.format('Measure', 'Results'))  # The header of table
            print('-------------------------------------')
            print('{}'.format('Mean:'), '{:>32}'.format('{:0.2f}').format(myMean(numbers)), '\n'
                '{}'.format('Mean:'), '{:>32}'.format('{:0.2f}').format(myMedian(numbers)), '\n'
                '{}'.format('Mode:'), '{:>32}'.format('{:0.2f}').format(myMode(numbers)), '\n'
                '{}'.format('Std Dev (Sample):'),'{:>20}'.format('{:0.2f}').format(mySt(numbers)), '\n'
                '{}'.format('Variance (Sample):'),'{:>17}'.format('{:0.2f}').format(myVa(numbers)), '\n'
                '{}'.format('Minimum:'),'{:>26}'.format(myMi(numbers)), '\n'
                '{}'.format('Maximum:'),'{:>26}'.format(myMa(numbers)), '\n'
                '{}'.format('Range:'),'{:>28}'.format(myRa(numbers)), '\n'
                '{}'.format('Sum:'),'{:>30}'.format(mySu(numbers)), '\n'
                '{}'.format('Count:'),'{:>28}'.format(myCo(numbers))) 
            print('')
            
            'Exit file and thank users.'    
        else:
            print('Thank you. DSA closing')
            inFile = open("2.txt", "r")
            count_file = inFile.read()
            inFile.close()
            for i in range(1,count_file):  # Count the number of files that have been analyzed.
                count_file += 1
            print('Files analyzed:', count_file) 
            print('')
            outFile = open("2.txt", "w")
            outFile.write(count_file)
            outFile.close()
            break
if __name__ == "__main__":
    main()