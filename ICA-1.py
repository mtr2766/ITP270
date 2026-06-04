#!/usr/bin/env python3

# Name: Matthew Runner
# ID: mtr2766

#============================
# Problem 1: Comment Practice
#============================

# This is a single line comment.

"""
This is a multi-line comment.
It can be more than one line.
Here I would describe the function or module
"""
single_quoted = 'Hello, world!'
double_quoted = "Hello, world!"
triple_quoted = '''Hello,
world'''

print(single_quoted, double_quoted, triple_quoted)

x = 10 # I can also add comments in-line.
y = 20 # Another in-line comment.

# Here I describe that below will print the values for x and y.
print("x =", x)
print("y =", y)

#================================
# Problem 2: String Concatenation
#================================

#Taking first name and last name input from user.
string1 = input("Enter your first name: ")
string2 = input("Enter your last name: ")

# Concatenate the first and last names into one string named "result".
result = string1 + string2

print("Your full name is:", result)

#===============================
# Problem 3: Simple Calculation
#===============================

# Here I will take two numbers as input and convert them to flaots.
print("Let's find the addition and multiplication of two numbers!")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Below we perform addition
addition = num1 + num2

# Below we perform multiplication
multiplication = num1 * num2

# Print values for verification
print("Addition:", addition)
print("Multiplication:", multiplication)

#==============================
# Problem 4: Exponent Calculation
#==============================

# Take an input number ffrom the user
print("Let's find the square of a number!")
number = float(input("Enter a number: "))

# Below we calculate the square using the operator **
square = number ** 2

# Print for verification
print("The square of", number, "is", square)

#===========================
# Problem 5: Modulo Practice
#===========================

# Take two numbers as input, dividend and divisor
print("Let's find the remainder for two numbers!")
dividend = float(input("Enter the dividend: "))
divisor = float(input("Enter the divisor: "))

# Here we will use the % operator, or modulo, to find remainder
remainder = dividend % divisor

print("The remainder of", dividend, "/", divisor, "is", remainder)
