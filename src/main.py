#Copyright (C), 2023-2024, bl33h
#FileName: main.py
#Author: Sara Echeverria, Melissa Perez, Alejandro Ortega
#Version: I
#Creation: 23/08/2023
#Last modification: 24/09/2023

from minAFD import AFDMinimizer
from regexToPostfix import regexToPostfix
from regex2afn import Regex2AFNConverter
from regex2afn import *
from afn2afd import *
import sys

# Define los nombres de los archivos para cada resultado
nfa_output_file = "nfa_output.txt"
postfix_output_file = "postfix_output.txt"
afd_output_file = "afd_output.txt"

# alphabet and regex expression
alphabet = "abce*+10"  # modify this according to your needs
epsilon = 'ε'  # Utiliza el carácter epsilon directamente

print("\n* Project 1 - Automata Generator *")
# prompt the user to enter a regular expression
expression = input("enter the regular expression: ")

exit = True

while exit:
    option = input("\n--------------------\nSelect an option:\n (1)Regex to postfix\n (2)Regex to AFN\n (3)From AFN to AFD\n (4)Min AFD\n (5)Simulation of AFN, AFD, and min AFD\n (6)Exit\n-------------------- \n>>> ")

    if option == "1":
        # Convert the infix regular expression to postfix
        postfix_expression = regexToPostfix(alphabet, expression, epsilon)
        # Print results
        result = postfix_expression.getResult().replace('\u03b5', 'epsilon')
        print("Postfix expression:", result)

        # Guarda el resultado en el archivo
        with open(postfix_output_file, "w", encoding="utf-8") as file:
            file.write(result)
            print("Result written to", postfix_output_file)

    if option == "2":
        postfix_expression = regexToPostfix(alphabet, expression, epsilon).getResult()
        converter = Regex2AFNConverter(epsilon)
        nfa = converter.convert2NFA(postfix_expression)
        
        # Redirige la salida estándar al archivo nfa_output_file
        with open(nfa_output_file, "w", encoding="utf-8") as file:
            sys.stdout = file
            converter.print_nfa(nfa)
            sys.stdout = sys.__stdout__  # Restaura la salida estándar
            
            print("Result written to", nfa_output_file)

    if option == "3":
        afd_results = afd_instance.print_afd_info()
        
        # Guarda los resultados en el archivo
        with open(afd_output_file, "w", encoding="utf-8") as file:
            sys.stdout = file
            print(afd_instance)
            sys.stdout = sys.__stdout__  # Restaura la salida estándar

    if option == "4":
        postfix_expression = regexToPostfix(alphabet, expression, epsilon).getResult()
        converter = Regex2AFNConverter(epsilon)
        nfa = converter.convert2NFA(postfix_expression)
        minimizer = AFDMinimizer()
        minDFA = minimizer.minimizeAFD(symbols, transitions, start, end)
        minimizer.print_min_dfa(minDFA)
    
    if option == "5":
        print("Redirecting output to text files.")

    if option == "6":
        exit = False        exit = False
        
states = [0, 1, 2, 3, 4]
symbols = ["a", "b"]
transitions = [
    {"a": 1, "b": 2},
    {"a": 1, "b": 3},
    {"a": 1, "b": 2},
    {"a": 1, "b": 4},
    {"a": 1, "b": 2},
]
start = 0
end = {4}