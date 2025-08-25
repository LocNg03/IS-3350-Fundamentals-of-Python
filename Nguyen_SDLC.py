"""""
Program: SDLC Assignment 1
Author: Loc Nguyen
Last Date Modified: 04/03/2022

The purpose of this assignment in the maintenance step fixes the problems of the previous code.
"""""
import pandas as pd
import matplotlib.pyplot as plt
import statistics

def new_func():
    'Open the file csv.'
    print('')
    #Read the csv file.
    df = pd.read_csv('insurance.csv')  

    #Display the first 20 value line in the data to the terminal.
    print (df.head(21)) 

    'Import and calculate the data'
    #The histogram of the data
    bmi = df.bmi
    charges = df.charges
    
    #Calculate the mean of BMI and charges
    mean_bm = statistics.mean(df.bmi)
    mean_ch = statistics.mean(df.charges)

    'Display the chart.'
    plt.bar(bmi, charges)
    plt.xlabel('BMI', fontsize=12, color='red')  # Title, font size, color
    plt.ylabel('Charges', fontsize=12, color='red') #Title, font size, color
    plt.title('The value of BMI and Charges', fontsize=14, color='red') #The title

    'Display the mean of charges and BMI.'
    # Display the mean of charge in the data value.
    plt.text(16, 52000, r'Mean charge = ' + '{:.8}'.format(str(mean_ch)))

    # Display the mean of BMI in the data value.
    plt.text(16, 57000, r'Mean BMI = ' + '{:.5}'.format(str(mean_bm)))

    #Format the number size of xlabel (from 15 to 54) and ylabel (from 1100 to 65000)
    plt.axis([15, 54, 1100, 65000]) 
    
    #Display grid
    plt.grid(True) 
    plt.show()
new_func()