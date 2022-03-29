# Student name: Jingxuan Feng
# Student number: s3843790


#!/bin/python3
# EXERCISE 1

# Get inputs from user
username = input("What is your name?")
input_float = float(input("Enter a float:"))
input_integer = int(input("Enter a integer:"))


# Function for calculating product
def product(float_value, integer_value):
    return float_value * integer_value


# Use function & get result
product_result = product(input_float, input_integer)


# Print according to spec requirements
print("Hello " + username + " !!!")
print("The product is:", product_result)



# EXERCISE 2

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
else:
    if(income <= 45000):
        ammount_of_tax = income * 0.19
    else:
        if(income > 45000):
            ammount_of_tax = income * 0.32


# Output results
if(ammount_of_tax == 0):
    print("you will pay no tax")
else:
    print("you will pay", ammount_of_tax)



# EXERCISE 3

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




