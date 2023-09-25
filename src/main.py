#Copyright (C), 2023-2024, bl33h
#FileName: main.py
#Author: Sara Echeverria, Melissa Perez, Alejandro Ortega
#Version: I
#Creation: 23/08/2023
#Last modification: 24/09/2023

from regexToPostfix import regexToPostfix
from regex2afn import Regex2AFNConverter
from afn2afd import AFN2AFDConverter

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
        converter = Regex2AFNConverter(epsilon, concat_operator="^")
        afn = converter.convert2NFA(postfix_expression)
        symbols = afn[0]
        states = afn[1]
        start = afn[2]
        end = afn[3]

        print("Inputs:", symbols)
        print("AFN transitions:", states)
        print("\nTransition table:")
        print("States:\t| Transitions:")
        for i in range(len(states)):
            state = "->{}".format(i) if i == start else "*{}".format(i) if i == end else i
            print("{: >3}:\t| {}".format(state, states[i]))

    if option == "3":
        # Convertir la expresión regular a postfix
        postfix_expression = regexToPostfix(alphabet, expression, epsilon).getResult()
        converter = Regex2AFNConverter(epsilon, concat_operator="^")
        afn = converter.convert2NFA(postfix_expression)
        symbols = afn[0]
        
        # Corregir la representación de nfa_states si es necesario
        # (asegúrate de que las transiciones sean diccionarios con conjuntos de estados)
        for i in range(len(afn[1])):
            for key, value in afn[1][i].items():
                if not isinstance(value, set):
                    afn[1][i][key] = {value}
        
        nfa_states = afn[1]
        nfa_start = afn[2]
        nfa_end = afn[3]

        print("Inputs:", symbols)
        print("AFN transitions:", nfa_states)

        # Convertir el AFN a AFD utilizando AFN2AFDConverter
        afd_converter = AFN2AFDConverter(epsilon)
        afd_keys, afd_transitions, afd_start, afd_accept = afd_converter.convert2DFA(symbols, nfa_states, nfa_start, nfa_end)

        # Mostrar las transiciones del AFD
        print("\nAFD Transitions:")
        for state, transitions in afd_transitions.items():
            print(f"State {state}:")
            for symbol, target_state in transitions.items():
                print(f"  {symbol} -> {target_state}")


    
    if option == "4":
        print("")
    
    if option == "5":
        print("")
    
    if option == "6":
        exit = False