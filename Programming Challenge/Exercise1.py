#!/bin/python3
# EXERCISE 1
# Student name: Jingxuan Feng
# Student number: s3843790

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