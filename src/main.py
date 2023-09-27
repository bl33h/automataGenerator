#Copyright (C), 2023-2024, bl33h
#FileName: main.py
#Author: Sara Echeverria, Melissa Perez, Alejandro Ortega
#Version: I
#Creation: 23/08/2023
#Last modification: 24/09/2023

from regexToPostfix import regexToPostfix
from regex2afn import Regex2AFNConverter
from regex2afn import *
from afn2afd import *

# alphabet and regex expression
alphabet = "abce*+10"  # modify this according to your needs
epsilon = 'e'

print("\n* Project 1 - Automata Generator *")
# prompt the user to enter a regular expression
expression = input("enter the regular expression: ")

exit = True

while exit:
    option = input("\n--------------------\nSelect an option:\n (1)Regex to postfix\n (2)Regex to AFN\n (3)From AFN to AFD\n (4)Min AFD\n (5)Simulation of AFN, AFD and min AFD\n (6)Exit\n-------------------- \n>>> ")

    if option == "1":
        # Convert the infix regular expression to postfix
        postfix_expression = regexToPostfix(alphabet, expression, "e")
        # print results
        print("Postfix expression:", postfix_expression.getResult())

    if option == "2":
        postfix_expression = regexToPostfix(alphabet, expression, epsilon).getResult()
        converter = Regex2AFNConverter("ε")
        nfa = converter.convert2NFA(postfix_expression)
        converter.print_nfa(nfa)

    if option == "3":
         print_afd_results()
        #postfix_expression = regexToPostfix(alphabet, expression, epsilon).getResult()
        #converter = Regex2AFNConverter(epsilon, concat_operator="^")
        #afn = converter.convert2NFA(postfix_expression)
        #symbols = afn[0]
        
        # Modifica nfa_states para convertirlo en un diccionario
        #nfa_states = {}
        #for i, state_transitions in enumerate(afn[1]):
            #nfa_states[i] = state_transitions

        #nfa_start = afn[2]
        #nfa_end = afn[3]

        #print("Inputs:", symbols)
        #print("AFN transitions:", nfa_states)

        # Convertir el AFN a AFD utilizando AFN2AFDConverter
        #afd_converter = AFN2AFDConverter(epsilon)
        #afd_result = afd_converter.convert2DFA(symbols, nfa_states, nfa_start, [nfa_end])

        # Mostrar los componentes del AFD resultante
        #print("\nAFD Components:")
        #print("Estados:", afd_result["Estados"])
        #print("Simbolos:", afd_result["Simbolos"])
        #print("Inicio:", afd_result["Inicio"])
        #print("Aceptacion:", afd_result["Aceptacion"])
        #print("Transiciones:", afd_result["Transiciones"])
    
    if option == "4":
        print("")
    
    if option == "5":
        print("")
    
    if option == "6":
        exit = False