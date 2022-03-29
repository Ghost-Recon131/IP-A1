#!/bin/python3
# EXERCISE 2
# Student name: Jingxuan Feng
# Student number: s3843790

# Ask for user input & use try catch, if exception thrown, program prints message and exits
try:
    income = float(input("Enter your income: "))
except:
    print("You did not enter a proper number!")
    quit()


# Define variables for storing amount of tax to be paid
ammount_of_tax = None

# If statements to determine amount of tax to be paid
if(income < 18200):
    ammount_of_tax = 0
elif(income <= 45000):
    ammount_of_tax = income * 0.19
elif(income > 45000):
    ammount_of_tax = income * 0.32


# Output results
if(ammount_of_tax == 0):
    print("you will pay no tax")
else:
    print("you will pay", ammount_of_tax)