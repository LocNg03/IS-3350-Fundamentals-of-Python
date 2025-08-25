"""""
Program: SDLC Assignment 2
Author: Loc Nguyen
Last Date Modified: 04/27/2022

The purpose of this assignment creates your own project with your own data set.
"""""
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sma
import statsmodels.formula.api as sms

# Create a Dataframe from the CSV file
SaYoPillow = pd.read_csv('SaYoPillow.csv')

# Rename 'sr.1' column to avoid an error being thrown in regression
SaYoPillow.rename(columns = {'sr.1':'sr1'}, inplace = True)

print("Hello!")
#Finding descriptive statistics
#Find Mean
print("------------------")
print("----- MEAN -------")
print("------------------")
print(SaYoPillow.mean())

#Find Median
print("\n------------------")
print("----- MEDIAN -----")
print("------------------")
print(SaYoPillow.median()) 

#Find Mode
print("\n------------------")
print("------ MODE ------")
print("------------------")
print(SaYoPillow.mode())

# Regression
SaYo_reg_model = sms.ols('sl ~ sr + rr + t + lm + bo + rem + sr1 + hr + sl', data = SaYoPillow).fit()
print("\n\n-------------------------------------------------")
print("-------------REGRESSION---------------------------")
print("--------------------------------------------------")
print(SaYo_reg_model.summary())

# ANOVA
one_way_anova = sma.stats.anova_lm(SaYo_reg_model, typ = 1) # Creating the ANOVA table
print("\n\n-------------------------------------------------")
print("---------------- ANOVA  (ONE WAY) ----------------")
print("--------------------------------------------------")
print(one_way_anova)

# PLOT
print('\n\n---------------------------')
print('-----------PLOT------------')
print('---------------------------')
SaYoPillow.plot(x = 'sr1', y = 'sl', figsize = (8,5))
plt.xlabel('sr1')
plt.ylabel('sl')
plt.title('Line Graph of srl against sl')
plt.show()