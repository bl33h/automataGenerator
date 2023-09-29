import re


class Regex2AFNConverter:
    
    def __init__(self, epsilon, concat_operator="."):
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
            elif i == self.concat_operator: # Concatenation
                r21, r22 = stack.pop()
                r11, r12 = stack.pop()
                c1 = r11
                c2 == r22
                stack.append([c1, c2])
                states[r12][self.epsilon] = r21
                if r21 == start:
                    start = r11
                if r12 == end:
                    end = r22
            elif i == "+":                  # Union
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
    
    def get_formatted_afn_params(self, afn: tuple) -> tuple:
        nfa_symbols, nfa_og_transitions, nfa_start, nfa_end = afn
        nfa_end = {nfa_end} # Convert end state to a set
        nfa_states = [i for i in range(len(nfa_og_transitions))]
        nfa_transitions = {}
        for i in range(len(nfa_og_transitions)):
            new_transition = {}
            for symbol in nfa_symbols:
                if nfa_og_transitions[i].get(symbol) is not None:
                    next_states = nfa_og_transitions[i].get(symbol)
                    new_transition[symbol] = [next_states] if not isinstance(next_states, tuple) else list(next_states)
            nfa_transitions[i] = new_transition
            
        return (nfa_symbols, nfa_states, nfa_transitions, nfa_start, nfa_end)
    
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
        
        print("\nEstado de Aceptación:")
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
