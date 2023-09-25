class AFN2AFDConverter:

    def __init__(self, epsilon):
        self.epsilon = epsilon

    def epsilon_closure(self, states, transitions):
        epsilon_closure_states = set(states)
        stack = list(states)

        while stack:
            state = stack.pop()
            if state in transitions and self.epsilon in transitions[state]:
                epsilon_transitions = transitions[state][self.epsilon]
                for epsilon_state in epsilon_transitions:
                    if epsilon_state not in epsilon_closure_states:
                        epsilon_closure_states.add(epsilon_state)
                        stack.append(epsilon_state)

        return frozenset(epsilon_closure_states)

    def convert2DFA(self, keys, nfa_states, nfa_start, nfa_end):
        dfa_states = set()
        dfa_transitions = {}
        dfa_start = self.epsilon_closure({nfa_start}, nfa_states)
        dfa_states.add(dfa_start)
        stack = [dfa_start]

        while stack:
            current_state = stack.pop()
            for key in keys:
                if key != self.epsilon:
                    next_states = set()
                    for nfa_state in current_state:
                        if key in set(nfa_states[nfa_state]):
                            next_states.update(nfa_states[nfa_state][key])
                    if next_states:
                        epsilon_closure_state = self.epsilon_closure(next_states, nfa_states)
                        if epsilon_closure_state not in dfa_states:
                            dfa_states.add(epsilon_closure_state)
                            stack.append(epsilon_closure_state)
                        if current_state not in dfa_transitions:
                            dfa_transitions[current_state] = {}
                        dfa_transitions[current_state][key] = epsilon_closure_state

                # Handle epsilon transitions and kleene star (*) operator
                next_states = set()
                for nfa_state in current_state:
                    if self.epsilon in nfa_states[nfa_state] or key == "*":
                        next_states.update(nfa_states[nfa_state][self.epsilon])
                if next_states:
                    epsilon_closure_state = self.epsilon_closure(next_states, nfa_states)
                    if epsilon_closure_state not in dfa_states:
                        dfa_states.add(epsilon_closure_state)
                        stack.append(epsilon_closure_state)
                    if current_state not in dfa_transitions:
                        dfa_transitions[current_state] = {}
                    dfa_transitions[current_state][self.epsilon] = epsilon_closure_state

            dfa_accept = set()
            for state in dfa_states:
                for nfa_accept_state in nfa_end:
                    if nfa_accept_state in state:
                        dfa_accept.add(state)

            return (keys, dfa_transitions, dfa_start, dfa_accept)
