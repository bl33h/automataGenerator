import re


class Regex2AFNConverter:
    
    def __init__(self, epsilon, concat_operator="^"):
        self.epsilon = epsilon
        self.concat_operator = concat_operator
        
    def convert2NFA(self, postfix_expression):
        regex = postfix_expression

        keys = list(set(re.sub('[^A-Za-z0-9]+', '', regex) + self.epsilon))

        states = []
        stack = []
        start = 0
        end = 1
        counter = -1
        c1 = 0
        c2 = 0

        for i in regex:
            if i in keys:                   # Terminal symbol
                counter = counter+1
                c1 = counter
                counter = counter+1
                c2 = counter
                states.append({})
                states.append({})
                stack.append([c1, c2])
                states[c1][i] = c2
            elif i == '*':                  # Kleen star
                r1, r2 = stack.pop()
                counter = counter+1
                c1 = counter
                counter = counter+1
                c2 = counter
                states.append({})
                states.append({})
                stack.append([c1, c2])
                states[r2][self.epsilon] = (r1, c2)
                states[c1][self.epsilon] = (r1, c2)
                if start == r1:
                    start = c1
                if end == r2:
                    end = c2
            else:                           # Union
                counter = counter+1
                c1 = counter
                counter = counter+1
                c2 = counter
                states.append({})
                states.append({})
                r11, r12 = stack.pop()
                r21, r22 = stack.pop()
                stack.append([c1, c2])
                states[c1][self.epsilon] = (r21, r11)
                states[r12][self.epsilon] = c2
                states[r22][self.epsilon] = c2
                if start == r11 or start == r21:
                    start = c1
                if end == r22 or end == r12:
                    end = c2
        
        return (keys, states, start, end)
    
    def print_nfa(self, nfa):
        keys, states, start, end = nfa
        print("Estados:")
        for i in range(len(states)):
            print(f"Estado {i}")
        
        print("\nSímbolos:")
        for key in keys:
            print(key)
        
        print("\nEstado Inicial:")
        print(start)
        
        print("\nEstados de Aceptación:")
        print(end)
        
        print("\nTransiciones:")
        for i, state in enumerate(states):
            for symbol, next_state in state.items():
                if isinstance(next_state, tuple):
                    for ns in next_state:
                        print(f"Estado {i} -> Estado {ns} con símbolo '{symbol}'")
                else:
                    print(f"Estado {i} -> Estado {next_state} con símbolo '{symbol}'")
    
    def process_input(input_strings, nfa):
        keys, states, start, end = nfa
        for input_string in input_strings:
            current_states = {start}  # Inicialmente, el estado actual es el estado inicial
            for symbol in input_string:
                next_states = set()
                for state in current_states:
                    if symbol in states[state]:
                        transition = states[state][symbol]
                        if isinstance(transition, tuple):
                            next_states.update(transition)
                        else:
                            next_states.add(transition)
                current_states = next_states
            # Después de procesar la cadena, verifica si el estado actual está en el estado de aceptación
            if end in current_states:
                print(f"'{input_string}' SÍ es aceptada")
            else:
                print(f"'{input_string}' No es aceptada")
