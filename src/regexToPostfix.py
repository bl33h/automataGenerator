#Copyright (C), 2023-2024, bl33h
#FileName: regexToPostfix.py (shunting yard algorithm implementation)
#Author: Sara Echeverria, Melissa Perez, Alejandro Ortega
#Version: I
#Creation: 23/08/2023
#Last modification: 03/09/2023

class regexToPostfix:
    def __init__(self, alphabet, expression, epsilon):
        self.alphabet = alphabet
        self.expression = expression
        self.epsilon = epsilon
        self.transformedExpression = self.transformExpression()
        self.tokens = self.tokenize(self.transformedExpression)
        self.result = self.shuntingYard()

    def __str__(self):
        data = [
            f"Expression: {self.expression}",
            f"Transformed Expression: {self.transformedExpression}",
            f"Tokens: {self.tokens}",
            f"Result: {self.result}"
        ]
        return "\n".join(data)

    def transformExpression(self):
        transformed = ""
        for i, char in enumerate(self.expression):
            if i < len(self.expression) - 1:
                transformed += char
                nextChar = self.expression[i + 1]
                # should_concat_literals = char in self.alphabet and nextChar in self.alphabet and nextChar != "+" and nextChar != "*"
                should_concat_literals = char.isalnum() and nextChar.isalnum()
                should_concat_kleen_star = char == "*" and (nextChar in self.alphabet or nextChar == "(") and nextChar != "+"
                if should_concat_literals or should_concat_kleen_star:
                    transformed += "."
            else:
                transformed += char
        return transformed

    def tokenize(self, expression):
        return list(expression)  # Divide la expresión transformada en caracteres individuales.

    def getPrecedence(self, operator):
        precedence = {
            "*": 3,
            ".": 2,
            "+": 1
        }
        return precedence.get(operator, 0)  # Obtiene la precedencia de un operador.

    def shuntingYard(self):
        output = []
        stack = []
        for token in self.tokens:
            if token.isalnum():
                output.append(token if token != self.epsilon else "\u03b5")
            elif token == "(":
                stack.append(token)  # Si es un paréntesis izquierdo, agregarlo a la pila.
            elif token == ")":
                # Mientras haya operadores en la pila, sacarlos y agregarlos a la salida hasta encontrar un "(".
                while stack[-1] != "(":
                    output.append(stack.pop())
                stack.pop()  # Sacar el "(" de la pila.
            else:
                # Mientras haya operadores en la pila con mayor o igual precedencia, sacarlos y agregarlos a la salida.
                while stack and self.getPrecedence(stack[-1]) >= self.getPrecedence(token):
                    output.append(stack.pop())
                stack.append(token)  # Agregar el operador actual a la pila.

        # Vaciar la pila y agregar los operadores restantes a la salida.
        while stack:
            output.append(stack.pop())

        return "".join(output)

    def getResult(self):
        return self.result