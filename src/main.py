#Copyright (C), 2023-2024, bl33h
#FileName: main.py
#Author: Sara Echeverria, Melissa Perez, Alejandro Ortega
#Version: I
#Creation: 23/08/2023
#Last modification: 03/09/2023

from regexToPostfix import regexToPostfix

# alphabet and regex expression
alphabet = "abce*+10" # modify this according to your needs

# prompt the user to enter a regular expression
expression = input("enter the regular expression: ")

# shunting yard algorithm instance in 'regexToPostfix' file
shunting_yard = regexToPostfix(alphabet, expression, "e")

# print results
print(shunting_yard)
print("postfix expression:", shunting_yard.getResult())
