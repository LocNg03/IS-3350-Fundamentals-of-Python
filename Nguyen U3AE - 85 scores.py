"""""
Program: NguyenU3AE
Author: Loc Nguyen
Last Date Modified: 02/13/2022

The purpose of this assignment trains the loop statements. 
"""
print("                        VCA Running                             ") # Welcome dialogue
name = input("Please provide the name you would like to use for this session: ") # Displays the string prompt and waits for keyboard input.
print("Hello,", name + ". Welcome to the Value Conversion Application (VCA).")  
choice = input("Do you need instructions " + name + " (Y/N): ") # Displays the string prompt and waits for keyboard input.
if choice == 'y' or choice == 'Y' or choice == "Yes": # Use if to generate conditionals for displaying "print" sentences below. 
  print(" - Please enter the value and hit the Enter key.") 
  print(" - The application will ask you for decimal value that is between 0 and 255.") 
  print(" - The application will respond with the binary and hexadecimal equivalents.") 
  print(" - The application will continue to ask you for values to convert.") 
  print(" - When you are ready to exit, enter the letter 'x'.") 
  print(" - Upon exiting, the application will print a handy conversion table.") 
EnterKey = input("When you are ready to start converting values, hit the Enter key.") # Displays the string prompt and waits for keyboard input.

# This is the main step in a whole assignment because the code below shows how to convert decimal, binary, hexadecimal and using the loop. 
while True: # While creates constitute a conditional loop. 
  a = input("Please enter a positive integer to convert (enter 'x' to end): ") # Displays the string prompt and waits for keyboard input.
  if a == 'x': # This is conditional of "a" 
    break # This stops the loop when is typed 'x'.  
  else:
    d = int(a) # Converts a (a = input) string  of digits to an integer value
    bina = bin(d)[2:] # Convert a base 10 number to binary (base 16),  omitting the first two characters.
    hexa = hex(d)[2:] # Convert a base 10 number to hexadecimal (base 16),  omitting the first two characters.
    print("Result:", d, "equals", bina, "in Binary", "and", hexa, "in Hexadecimal notation") 
print("Thank you", name, "for using the VCA. Here is a handy table:") # Exit/ Thank you dialogue: appear when the loop are done. 
print("-----------------------------------------")
print("{:>9s} {:>11s} {:>17s}".format("Decimal", "Binary", "Hexadecimal")) # Table's header. 
print("-----------------------------------------")
for t in range(0, 14): # Use "for... range" to generate the loop from 0 to 14.  
  de = t # Equivalent to Decimal value convert to Binary and Hexadecimal.
  bina = bin(de)[2:] # Convert a base 10 number to binary (base 16),  omitting the first two characters.
  hexad = hex(de)[2:].upper() # Convert a base 10 number to hexadecimal (base 16),  omitting the first two characters and upper characters.
  print("{:<17}".format("{:5.0f}".format(de)), 
        "{:<16}".format("{:8s}".format(bina)), 
        "{:<16}".format("{:4.2s}".format(hexad)))