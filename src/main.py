#Copyright (C), 2023-2024, bl33h
#FileName: main.py
#Author: Sara Echeverria, Melissa Perez, Alejandro Ortega
#Version: I
#Creation: 23/08/2023
#Last modification: 03/09/2023

from regexToPostfix import regexToPostfix

# alphabet and regex expression
alphabet = "abc*|"
expression = "(a|b)*c"

# shunting yard algorithm instance in 'regexToPostfix' file
shuntingYardExpression = regexToPostfix(alphabet, expression)

# print results
print(str(regexToPostfix))
print(f"initial expression: " + expression)
print("postfix expression:", shuntingYardExpression.getResult())