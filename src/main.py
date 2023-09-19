#Copyright (C), 2023-2024, bl33h
#FileName: main.py
#Author: Sara Echeverria, Melissa Perez, Alejandro Ortega
#Version: I
#Creation: 23/08/2023
#Last modification: 15/09/2023

import networkx as nx
from regexToPostfix import regexToPostfix
from afn import PostfixToNFA
import matplotlib.pyplot as plt

# alphabet and regex expression
alphabet = "abce*+"
expression = "a*(a+b)*e*"
epsilon = "\u03b5"

# Shunting Yard Algorithm
shunting_yard = regexToPostfix(alphabet, expression, epsilon)
postfix_expression = shunting_yard.getResult()
print(shunting_yard)
print("postfix expression:", shunting_yard.getResult())

# Create the NFA
postfix_to_nfa = PostfixToNFA(postfix_expression, alphabet, epsilon)
nfa_graph = postfix_to_nfa.createNFA()

# Assign labels to nodes and edges
labels = {n: data.get("label", "") for n, data in nfa_graph.nodes(data=True)}
edge_labels = {(u, v): data.get("label", "") for u, v, data in nfa_graph.edges(data=True)}

# Visualize the NFA with labels
pos = nx.spring_layout(nfa_graph)  # You can use a different layout if needed

# Draw the graph with labels
nx.draw(nfa_graph, pos, with_labels=True, labels=labels, node_size=800, node_color="lightblue")
nx.draw_networkx_edge_labels(nfa_graph, pos, edge_labels=edge_labels, label_pos=0.3)
plt.show()
