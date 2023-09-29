from regex2afn import *

from collections import deque

class NFAtoAFDConverter:
    def __init__(self, nfa_states, nfa_symbols, nfa_transitions, nfa_start_state, nfa_accept_states, epsilon="\u03b5"):
        self.nfa_states = nfa_states
        self.nfa_symbols = nfa_symbols
        self.nfa_transitions = nfa_transitions
        self.nfa_start_state = nfa_start_state
        self.nfa_accept_states = nfa_accept_states
        self.afd_states = set()
        self.afd_symbols = set()
        self.afd_transitions = {}
        self.afd_start_state = None
        self.afd_accept_states = set()
        self.epsilon = epsilon
        self.convert_nfa_to_afd()

    def epsilon_closure(self, states):
        epsilon_closure_set = set(states)
        stack = list(states)
        while stack:
            state = stack.pop()
            if state in self.nfa_transitions and self.epsilon in self.nfa_transitions[state]:
                epsilon_transitions = self.nfa_transitions[state][self.epsilon]
                for epsilon_state in epsilon_transitions:
                    if epsilon_state not in epsilon_closure_set:
                        epsilon_closure_set.add(epsilon_state)
                        stack.append(epsilon_state)
        return list(epsilon_closure_set)

    def convert_nfa_to_afd(self):
        start_state = self.epsilon_closure([self.nfa_start_state])
        state_queue = deque()
        state_queue.append(start_state)
        state_mapping = {tuple(start_state): start_state}

        while state_queue:
            current_state = state_queue.popleft()
            self.afd_states.add(tuple(current_state))
            if any(state in self.nfa_accept_states for state in current_state):
                self.afd_accept_states.add(tuple(current_state))
            for symbol in self.nfa_symbols:
                if symbol == self.epsilon:
                    continue
                new_state = []
                for nfa_state in current_state:
                    if nfa_state in self.nfa_transitions and symbol in self.nfa_transitions[nfa_state]:
                        new_state.extend(self.nfa_transitions[nfa_state][symbol])
                if new_state:
                    epsilon_closure_set = self.epsilon_closure(new_state)
                    if tuple(epsilon_closure_set) not in state_mapping:
                        state_queue.append(epsilon_closure_set)
                        state_mapping[tuple(epsilon_closure_set)] = epsilon_closure_set
                    self.afd_transitions[tuple(current_state)] = self.afd_transitions.get(tuple(current_state), {})
                    self.afd_transitions[tuple(current_state)][symbol] = tuple(epsilon_closure_set)

        self.afd_start_state = tuple(start_state)
        self.afd_symbols = [symbol for symbol in self.nfa_symbols if symbol != self.epsilon]

    def get_afd_params(self):
        return (
            list(self.afd_states),
            self.afd_symbols,
            self.afd_transitions,
            self.afd_start_state,
            self.afd_accept_states
        )

class AFD:
    def __init__(self):
        self.states = set()
        self.symbols = set()
        self.transitions = {}
        self.start_state = None
        self.accept_states = set()

    def add_states(self, states):
        self.states.update(states)

    def add_symbols(self, symbols):
        self.symbols.update(symbols)

    def add_transition(self, from_state, symbol, to_state):
        self.transitions[from_state] = self.transitions.get(from_state, {})
        self.transitions[from_state][symbol] = to_state

    def set_start_state(self, state):
        self.start_state = state

    def add_accept_states(self, states):
        self.accept_states.update(states)

    def is_accepted(self, state):
        return state in self.accept_states

    def process_input(self, input_string):
        current_state = self.start_state
        for symbol in input_string:
            if symbol not in self.symbols:
                return False
            if current_state in self.transitions and symbol in self.transitions[current_state]:
                current_state = self.transitions[current_state][symbol]
            else:
                return False
        return self.is_accepted(current_state)
    
    def print_afd_info(self):
        print("Estados del AFD:")
        for state in self.states:
            print(state)
        
        print("\nSímbolos del AFD:")
        for symbol in self.symbols:
            print(symbol)
        
        print("\nTransiciones del AFD:")
        for from_state, transitions in self.transitions.items():
            for symbol, to_state in transitions.items():
                print(f"De {from_state} a {to_state} con símbolo '{symbol}'")
        
        print("\nEstado Inicial del AFD:")
        print(self.start_state)
        
        print("\nEstados de Aceptación del AFD:")
        for accept_state in self.accept_states:
            print(accept_state)

