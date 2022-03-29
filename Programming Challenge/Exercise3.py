#!/bin/python3
# EXERCISE 3
# Student name: Jingxuan Feng
# Student number: s3843790

# Get user inputs
try:
    divisor1 = int(input("What is the first divisor (int): "))
    divisor2 = int(input("What is the second divisor (int): "))
    lower_bound = int(input("What is the lower bound (int): "))
except:
    print("Invalid input, integer expected, quitting program")
    quit()

# Upper bound as per specs
upper_bound = 42


# Function for calculating if number is dividable by divisor
def is_number_divisible(number, divisor):
    return bool(number % divisor == 0)


# While loop check if lowerbound is divisible by divisors entered
while(lower_bound <= 42):
    if(is_number_divisible(lower_bound, divisor1)):
        print(str(lower_bound) + " is divisible by " + str(divisor1))
    if(is_number_divisible(lower_bound, divisor2)):
        print(str(lower_bound) + " is divisible by " + str(divisor2))
    lower_bound = lower_bound + 1
