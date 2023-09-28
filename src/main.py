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
        postfix_expression = regexToPostfix(alphabet, expression, epsilon).getResult()
        converter = Regex2AFNConverter(epsilon)
        nfa = converter.convert2NFA(postfix_expression)
        nfa_symbols = nfa[0]
        nfa_states = [i for i in range(len(nfa[1]))]
        og_transitions = nfa[1]
        print("OG Transitions:", og_transitions)
        nfa_transitions = {}
        for i in range(len(og_transitions)):
            new_transition = {}
            for symbol in nfa_symbols:
                if og_transitions[i].get(symbol) is not None:
                    next_states = og_transitions[i].get(symbol)
                    new_transition[symbol] = [next_states] if not isinstance(next_states, tuple) else list(next_states)
            nfa_transitions[i] = new_transition
        print("NFA Transitions:", nfa_transitions)
        afdConverter = NFAtoAFDConverter(nfa_states, nfa_symbols, nfa_transitions, nfa[2], {nfa[3]})
        afdConverter.convert_nfa_to_afd()
        afd_results = afdConverter.get_afd_params()

        for result in afd_results:
            print(result)

        
        # Guarda los resultados en el archivo
        with open(afd_output_file, "w", encoding="utf-8") as file:
            sys.stdout = file
            #print(afd_instance)
            sys.stdout = sys.__stdout__  # Restaura la salida estándar

    if option == "4":
        postfix_expression = regexToPostfix(alphabet, expression, epsilon).getResult()
        converter = Regex2AFNConverter(epsilon)
        nfa = converter.convert2NFA(postfix_expression)
        minimizer = AFDMinimizer()
        
    if option == "5":
        print("Redirecting output to text files.")

    if option == "6":
        exit = False
        
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