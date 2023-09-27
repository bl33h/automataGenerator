class AFD:

    def __init__(self):
        self.states = set()
        self.symbols = set() 
        self.transitions = {}  
        self.start_state = None
        self.accept_states = set()

    def add_state(self, state):
        self.states.add(state)

    def add_symbol(self, symbol):
        self.symbols.add(symbol)

    def add_transition(self, from_state, symbol, to_state):
        if from_state not in self.states:
            self.add_state(from_state)
        if to_state not in self.states:
            self.add_state(to_state)
        if symbol not in self.symbols:
            self.add_symbol(symbol)
        if from_state not in self.transitions:
            self.transitions[from_state] = {}
        self.transitions[from_state][symbol] = to_state

    def set_start_state(self, state):
        self.start_state = state

    def add_accept_state(self, state):
        self.accept_states.add(state)

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

# Definición de los datos proporcionados

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

# Crear y configurar el AFD
afd = AFD()
afd.states = set(states)
afd.symbols = set(symbols)
for i, transition in enumerate(transitions):
    for symbol, to_state in transition.items():
        afd.add_transition(i, symbol, to_state)
afd.set_start_state(start)
afd.accept_states = end

# Imprimir los resultados del AFD
def print_afd_results():
    print("\nResultados AFD\n----------------")
    print("Estados:", afd.states)
    print("Símbolos:", afd.symbols)
    print("Estado inicial:", afd.start_state)
    print("Estados de aceptación:", afd.accept_states)
    print("Transiciones:")
    for from_state, transitions in afd.transitions.items():
        for symbol, to_state in transitions.items():
            print(f" ({from_state}, {symbol}, {to_state})")

    # Probando el AFD con cadenas de entrada
    print("\nIngreso de cadenas al autómata\n----------------")
    input_strings = ["ab", "aaab", "abb", "baba", "a", "b", ""]
    for input_string in input_strings:
        if afd.process_input(input_string):
            print(f"'{input_string}' SÍ es aceptada")
        else:
            print(f"'{input_string}' No es aceptada")