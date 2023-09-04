#Copyright (C), 2023-2024, bl33h
#FileName: regexToPostfix.py (shunting yard algorithm implementation)
#Author: Sara Echeverria, Melissa Perez, Alejandro Ortega
#Version: I
#Creation: 23/08/2023
#Last modification: 03/09/2023

class regexToPostfix:
    def __init__(self, alphabet, expression):
        self.alphabet = alphabet  # Conjunto de caracteres permitidos en la expresión regular.
        self.expression = expression  # La expresión regular en notación infix.
        self.transformedExpression = self.transformExpression()  # La expresión infix transformada.
        self.tokens = self.tokenize(self.transformedExpression)  # Lista de tokens en la expresión.
        self.result = self.shuntingYard()  # La expresión postfix resultante.

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
                # Agregar "^" entre literales contiguos o "*" y una letra para evitar ambigüedades.
                should_concat_literals = char in self.alphabet and self.expression[i + 1] in self.alphabet
                should_concat_kleen_star = char == "*" and self.expression[i + 1] in self.alphabet
                if should_concat_literals or should_concat_kleen_star:
                    transformed += "^"
            else:
                transformed += char
        return transformed

    def tokenize(self, expression):
        return list(expression)  # Divide la expresión transformada en caracteres individuales.

    def getPrecedence(self, operator):
        precedence = {
            "*": 3,
            "^": 2,
            "+": 1
        }
        return precedence.get(operator, 0)  # Obtiene la precedencia de un operador.

    def shuntingYard(self):
        output = []
        stack = []
        for token in self.tokens:
            if token in self.alphabet:
                output.append(token)  # Si es un carácter del alfabeto, agregarlo a la salida.
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

        return output  # La expresión postfix resultante.

    def getResult(self):
        return self.result