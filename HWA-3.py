#!/usr/bin/env python3
# Name: Matthew Runner
# ID: mtr2766

#=====================================
# Problem 1: Concatentate Name and Age
#=====================================

def name_age(name, age):
	return f"{name} is {age} years old."

print(name_age("Matt", 34))
print(name_age("Lucas", 12))

"""
# Taking user input instead of just calling name & x
name = str(input("What is your name? "))
x = int(input("What is your age? "))
print(name_age(name, x))
"""
#=============================
# Problem 2: Reverse Substring
#=============================

def reverse_substring(s, start, end):
	return s[start:end][::-1]

print(reverse_substring("ITP276", 1, 4))
print(reverse_substring("Matthew", 0, 5))
