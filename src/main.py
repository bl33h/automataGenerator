#Copyright (C), 2023-2024, bl33h
#FileName: main.py
#Author: Sara Echeverria, Melissa Perez, Alejandro Ortega
#Version: I
#Creation: 23/08/2023
#Last modification: 29/09/2023

from minAFD import AFDMinimizer
from regexToPostfix import regexToPostfix
from regex2afn import *
from afn2afd import *
import sys

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

# Define los nombres de los archivos para cada resultado
nfa_output_file = "nfaOutput.txt"
postfix_output_file = "postfixOutput.txt"
afd_output_file = "dfaOutput.txt"
min_afd_output_file = "minDfaOutput.txt"

# alphabet and regex expression
alphabet = "abced*+10"  # modify this according to your needs
epsilon = 'ε'  # Utiliza el carácter epsilon directamente
input_strings = ["ab", "100001", "abbcd", "baba", "10101", "b", ""]

print("\n* Project 1 - Automata Generator *")
# prompt the user to enter a regular expression
expression = input("enter the regular expression: ")

exit = True

while exit:
    option = input("\n--------------------\nSelect an option:\n (1)Regex to postfix\n (2)Regex to AFN\n (3)From AFN to AFD\n (4)Min AFD\n (5)Exit\n-------------------- \n>>> ")

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

        Regex2AFNConverter.process_input(input_strings, nfa)

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
        nfa_symbols, nfa_states, nfa_transitions, nfa_start, nfa_end = converter.get_formatted_afn_params(nfa)
        afdConverter = NFAtoAFDConverter(nfa_states, nfa_symbols, nfa_transitions, nfa_start, nfa_end)
        afdConverter.convert_nfa_to_afd()
        afd_results = afdConverter.get_afd_params()
        afd_formatted_results = afdConverter.get_formatted_afd_params()
        
        afd_instance = AFD()
        afd_instance.add_states(afd_results[0])
        afd_instance.add_symbols(afd_results[1])
        afd_instance.transitions = afd_results[2]
        afd_instance.set_start_state(afd_results[3])
        afd_instance.add_accept_states(afd_results[4])

        # Procesar las cadenas de entrada y mostrar los resultados
        print("\n---\nAnálsis de cadenas:")
        for input_string in input_strings:
            if afd_instance.process_input(input_string):
                print(f"'{input_string}' SÍ es aceptada")
            else:
                print(f"'{input_string}' No es aceptada")

        # Guarda los resultados en el archivo
        with open(afd_output_file, "w", encoding="utf-8") as file:
            sys.stdout = file
            afd_instance.print_afd_info()
            sys.stdout = sys.__stdout__  # Restaura la salida estándar

    if option == "4":
        postfix_expression = regexToPostfix(alphabet, expression, epsilon).getResult()
        converter = Regex2AFNConverter(epsilon)
        nfa = converter.convert2NFA(postfix_expression)
        minimizer = AFDMinimizer()
        min_afd = minimizer.minimizeAFD(symbols, transitions, start, end)

        # Muestra el AFD minimizado
        minimizer.print_min_dfa(min_afd)

        # Crea una instancia de AFD con los componentes de la tupla min_afd
        afd_instance = AFD()
        afd_instance.add_states(min_afd[0])
        afd_instance.add_symbols(min_afd[1])
        afd_instance.transitions = min_afd[2]
        afd_instance.set_start_state(min_afd[3])
        afd_instance.add_accept_states(min_afd[4])
        
        # Ahora procesa las cadenas de entrada con la instancia de AFD
        print("\n---\nAnálisis de cadenas:")
        for input_string in input_strings:
            if afd_instance.process_input([input_string]):
                print(f"'{input_string}' SÍ es aceptada")
            else:
                print(f"'{input_string}' No es aceptada")
        
    if option == "5":
        exit = False