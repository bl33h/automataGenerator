
class AFDMinimizer:
    
    def __init__(self):
        pass

    def printMinTable(self, minTable):
        for i in range(len(minTable)):
            print("{}: {}".format(i, minTable[i]))

    def markInitialStatePair(self, state_a: int, state_b: int, end: set) -> bool:    
        return (
            state_a < state_b and                       # States are over the diagonal of the matrix
            state_a in end and state_b not in end or    # Only one of the two states is an acceptance state
            state_a not in end and state_b in end
        )
        
    def markStatePair(self, state_a: int, state_b: int, minTable: list, symbols: list, transitions: list) -> bool:
        state_b += state_a + 1
        for symbol in symbols:
            # print("\tChecking for '{}' transitions".format(symbol))
            next_state_a = transitions[state_a].get(symbol)
            next_state_b = transitions[state_b].get(symbol)
            # print("\tTransition for {}: '{}'".format(state_a, next_state_a))
            # print("\tTransition for {}: '{}'".format(state_b, next_state_b))
            if next_state_a == next_state_b: 
                # print("\tSkipped pair ({}, {})".format(next_state_a, next_state_b))
                continue   # Discard state pairs in matrix diagonal
            i = next_state_a
            j = next_state_b
            # print("\ti:", i, "j:", j)
            if i > j:   # If the state pair is under diagonal, flip the state indexes
                i = next_state_b
                j = next_state_a
                # print("\tFlipped indices -> i:", i, "j:", j)
            if minTable[i][j - (i + 1)] == 1: return True
        return False
            
    def getNonDistinctStates(self, minTable: list) -> list:
            nonDistinctStates = []
            for i in range(len(minTable)):
                for j in range(len(minTable[i])):
                    if minTable[i][j] == 0: nonDistinctStates.append((i, j + i + 1))
            return nonDistinctStates 
        
    def getDistinctStates(self, minTable: list, states: list) -> list:
        distinctStates = []
        for i in range(len(states) - 1):
            print("i:", i)
            if 0 in minTable[i]: distinctStates.append(states[i])
        distinctStates.append(states[-1])
        return distinctStates 

    def minimizeAFD(self, symbols: list, transitions: list, start: int, end: set) -> tuple:
        minStart = start
        minEnd = end
        minStates = [i for i in range(len(transitions))]
        minTransitions = transitions.copy()
        minTable = []
        # Mark the initial states  
        for i in range(len(minStates) - 1):
            tempList = []
            for j in range(i + 1, len(minStates)):
                tempList.append(int(self.markInitialStatePair(i, j, minEnd)))
            minTable.append(tempList)
        
        # Copy the values from the initial table to newMinTable
        # This is not pretty but python won't let me just copy the table normally
        newMinTable = []
        for i in range(len(minTable)):
            temp = []
            for j in range(len(minTable[i])):
                temp.append(minTable[i][j])
            newMinTable.append(temp)
        newMinTable[0][0] = 1

        # Continue iterating to fill the table until minTable and newMinTable are equal
        while True:
            for i in range(len(newMinTable)):
                for j in range(len(newMinTable[i])):
                    if newMinTable[i][j] == 0:
                        newMinTable[i][j] = int(self.markStatePair(i, j, newMinTable, symbols, minTransitions))
            # Exit While loop if the previous table is equal to the new one
            if newMinTable == minTable: 
                break
            else: 
                minTable = newMinTable
        
        # Create the new AFD using only distinct states
        nonDistinctStates = self.getNonDistinctStates(minTable)
        for equivalentStates in nonDistinctStates:
            stateToRemove = equivalentStates[0]
            stateToKeep = equivalentStates[1]
            # Re-route transitions to stateToKeep
            for transition in minTransitions:
                for symbol in symbols:
                    if transition[symbol] == stateToRemove: transition[symbol] = stateToKeep
            # Remove stateToRemove
            minTransitions.remove(minTransitions[stateToRemove])
            minStates.remove(stateToRemove)
            # Set new start state if neccessary
            if minStart == stateToRemove: minStart = stateToKeep
            # Set new accept state(s) if necessary
            if stateToRemove in minEnd:
                minEnd.remove(stateToRemove)
                if stateToKeep not in minEnd: minEnd.add(stateToKeep)
        # Return the minimized DFA with the addition of the state array
        return (symbols, minStates, minTransitions, minStart, minEnd)
    
    def print_min_dfa(self, minDFA: tuple):
        symbols, states, transitions, start, end = minDFA
        
        print("ESTADOS =", set(states))
        print("SIMBOLOS =", set(symbols))
        print("INICIO =", set([start]))
        print("ACEPTACION =", set([end]) if not isinstance(end, set) else end)
        newTransitions = []
        for i in range(len(states)):
            for symbol in symbols:
                state = states[i]
                nexState = transitions[i].get(symbol)
                newTransitions.append((state, symbol, nexState))
        print("TRANSICIONES =", set(newTransitions))

# -----------------------------------
# Usage example
# -----------------------------------
# Regex: a+b
# Postif: ab+
# AFD:
#       a   b
# -> 0: 1   1
#  * 1: 2   2
#    2: 2   2

# states = [0, 1, 2, 3, 4]
# symbols = ["a", "b"]
# transitions = [
#     {"a": 1, "b": 2},
#     {"a": 1, "b": 3},
#     {"a": 1, "b": 2},
#     {"a": 1, "b": 4},
#     {"a": 1, "b": 2},
# ]
# start = 0
# end = {4}

# minimizer = AFDMinimizer()
# minAFD = minimizer.minimizeAFD(symbols, transitions, start, end)
# print(minAFD)