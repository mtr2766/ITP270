#!/usr/bin/env python3
# Name: Matthew Runner
# ID: mtr2766

#===========================
# Problem 1: Character Check
#===========================

def is_alpha_digit(char):
	# is_alpha returns TRUE if char. is a letter
	# is_digit returns TRUE if char. is a number
	return (char.isalpha(), char.isdigit())

# Running the function to check the character with input validation loop
while True:
	char= input("Enter a character: ")
	if len(char) == 1:
		print(is_alpha_digit(char))
		break
	else:
		print("Please enter only a single character.")

#=======================================
# Problem 2: String Length & First Char.
#=======================================

def string_info(string):
	length = len(string)

	# If the string is empty, return "None"
	if length == 0:
		first_char = None
	else:
		first_char = string[0]

	return (length, first_char)

string = input("Enter a word: ")
print(string_info(string))

#=============
# Count Vowels
#=============

def count_vowels(string):
	vowels = "aeiou" # Only using lowercase as we will convert the string input to lower later
	count = 0

	# Looping through each char., checking for a vowel, and adding 1 to counter if vowel
	for char in string:
		if char in vowels:
			count +=1
	return count

# Taking user input, converting to lower for ease of counting, calling count_vowel function to count vowels and return counter
string = input("Enter a word: ").lower()
print(count_vowels(string))
