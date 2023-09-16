import networkx as nx

class PostfixToNFA:
    def __init__(self, postfix_expression, alphabet, epsilon):
        self.postfix_expression = postfix_expression
        self.alphabet = alphabet
        self.epsilon = epsilon
        self.stack = []

    def createNFA(self):
        nfa_graph = nx.DiGraph()  # Crear el grafo del AFN

        for token in self.postfix_expression:
            if token.isalnum() or token == self.epsilon:
                # Crear dos nuevos nodos para representar el estado inicial y final.
                initial_state = nx.DiGraph()
                final_state = nx.DiGraph()

                # Agregar una transición desde el estado inicial al final con el símbolo actual.
                nfa_graph.add_edge(initial_state, final_state, label=token)

                # Apilar el par de nodos (estado inicial, estado final) en la pila.
                self.stack.append((initial_state, final_state))
            elif token == '^':
                # Obtener los dos últimos pares de nodos en la pila.
                state2_initial, state2_final = self.stack.pop()
                state1_initial, state1_final = self.stack.pop()

                # Conectar el estado1_final con el estado2_inicial con una transición epsilon.
                nfa_graph.add_edge(state1_final, state2_initial, label=self.epsilon)

                # Apilar el nuevo par de nodos (estado1_inicial, estado2_final) en la pila.
                self.stack.append((state1_initial, state2_final))
            elif token == '+':
                # Obtener los dos últimos pares de nodos en la pila.
                state2_initial, state2_final = self.stack.pop()
                state1_initial, state1_final = self.stack.pop()

                # Crear dos nuevos nodos para representar la concatenación.
                new_initial_state = nx.DiGraph()
                new_final_state = nx.DiGraph()

                # Conectar el nuevo estado inicial con los estados iniciales de state1 y state2 con transiciones epsilon.
                nfa_graph.add_edge(new_initial_state, state1_initial, label=self.epsilon)
                nfa_graph.add_edge(new_initial_state, state2_initial, label=self.epsilon)

                # Conectar los estados finales de state1 y state2 con el nuevo estado final con transiciones epsilon.
                nfa_graph.add_edge(state1_final, new_final_state, label=self.epsilon)
                nfa_graph.add_edge(state2_final, new_final_state, label=self.epsilon)

                # Apilar el par de nodos (new_initial_state, new_final_state) en la pila.
                self.stack.append((new_initial_state, new_final_state))

        # Al final, la pila debería contener un solo AFN completo.
        if len(self.stack) != 1:
            raise ValueError("La pila no contiene un solo AFN al final.")

        return nfa_graph
