# atomataGenerator
This project provides a Python-based tool for converting Non-Deterministic Finite Automata (NFA) to Deterministic Finite Automata (DFA) and subsequently minimizing the resulting DFA. It also includes functionality for converting regular expressions to NFAs.

<p align="center">
  <br>
  <img src="https://miro.medium.com/v2/resize:fit:640/1*BDs8D_Jtb7yKMAK86mKADg.gif" alt="pic" width="500">
  <br>
</p>
<p align="center" >
  <a href="#Files">Files</a> •
  <a href="#Features">Features</a> •
  <a href="#how-to-use">How To Use</a> 
</p>

## Files
- **afn2afd.py:**
  - Contains the NFA to DFA converter class.
- **main.py:**
  - The main application file that orchestrates the entire process, including input processing, NFA to DFA conversion, and minimization.

- **minAFD.py:**
  - Implements the AFDMinimizer class responsible for DFA minimization.
    
- **regex2afn.py:**
  - Defines the Regex2AFNConverter class for converting regular expressions to NFAs.

- **regexToPostfix.py:**
  - Implements the Shunting Yard algorithm for converting regular expressions to postfix notation.

## Features

The main features of the application include:
- Regex to NFA Conversion:
  - Converts a postfix regular expression into a Non-deterministic Finite Automaton (NFA).
  - Utilizes the Shunting Yard algorithm for parsing and evaluating postfix expressions.
  - Generates NFA states, transitions, and handles epsilon (ε) transitions.
    
- NFA to DFA Conversion:
  - Converts the Non-deterministic Finite Automaton (NFA) into a Deterministic Finite Automaton (DFA).
  - Computes epsilon closures and minimizes the number of states in the DFA.
  - Allows for processing input strings and determining their acceptance based on the DFA.
    
- DFA Minimization:
  - Minimizes the Deterministic Finite Automaton (DFA) to reduce the number of states while preserving language recognition.
  - Implements the Shunting Yard algorithm to evaluate regular expressions and convert them to postfix notation.


- Readable Output:
  - Provides clear and structured output, including information on states, symbols, transitions, the start state, and accept states.
  - Enables easy interpretation of automaton components for debugging and analysis.

## How To Use
To clone and run this application, you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/downloads/) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/bl33h/automataGenerator

# Open the folder
$ cd src

# Run de app
$ python main.py
```
