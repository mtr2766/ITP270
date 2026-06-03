#!/usr/bin/env python3
# Name: Matthew Runner
# ID: mtr2766

#=============================
# Problem 1:  Input and Output
#=============================

name = input("What is your name? ")
fav_num = int(input("What is your favourite number? "))
square = fav_num ** 2

print(f"Hello, name the square of your favourite number, {fav_num}, is {square}.")

#==============================================================
# Problem 2: Numeric Data Type Conversion and Formatting Output
#==============================================================

temp = float(input("What is the temperature in Celsius? "))
temp_f = (temp * 9 / 5) + 32
temp_k = temp + 273.15

print(f"{temp:.2f} degrees Celsius is {temp_f:.2f} in Farenheit and {temp_k:.2f} in Kelvin.")

