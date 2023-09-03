#Copyright (C), 2023-2024, bl33h
#FileName: regexToPostfix.py (shunting yard algorithm implementation)
#Author: Sara Echeverria, Melissa Perez, Alejandro Ortega
#Version: I
#Creation: 23/08/2023
#Last modification: 03/09/2023

class regexToPostfix:
    def __init__(self, alphabet, expression):
        self.alphabet = alphabet
        self.expression = expression
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
                should_concat_literals = char in self.alphabet and self.expression[i + 1] in self.alphabet
                should_concat_kleen_star = char == "*" and self.expression[i + 1] in self.alphabet
                if should_concat_literals or should_concat_kleen_star:
                    transformed += "^"
            else:
                transformed += char
        return transformed

    def tokenize(self, expression):
        return list(expression)

    def getPrecedence(self, operator):
        precedence = {
            "*": 3,
            "^": 2,
            "+": 1
        }
        return precedence.get(operator, 0)

    def shuntingYard(self):
        output = []
        stack = []
        for token in self.tokens:
            if token in self.alphabet:
                output.append(token)
            elif token == "(":
                stack.append(token)
            elif token == ")":
                while stack[-1] != "(":
                    output.append(stack.pop())
                stack.pop()
            else:
                while stack and self.getPrecedence(stack[-1]) >= self.getPrecedence(token):
                    output.append(stack.pop())
                stack.append(token)

        while stack:
            output.append(stack.pop())

        return output

    def getResult(self):
        return self.result