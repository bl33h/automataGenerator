import re
# precedence level of supported operators.
PRECEDENCE = {
    '^': 4, # highest precedence level
    '*': 3,
    '/': 3,
    '+': 2,
    '-': 2,
    '(': 1,
}

def infixToPostfix(expr):
    tokens = re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\^\+\*\-\/])", expr)
    stack = []
    postfix = []
    
    for token in tokens:
        # If the token is an operand, then do not push it to stack. 
        # Instead, pass it to the output.
        if token.isalnum():
            postfix.append(token)
    
        # If your current token is a right parenthesis
        # push it on to the stack
        elif token == '(':
            stack.append(token)

        # If your current token is a right parenthesis,
        # pop the stack until after the first left parenthesis.
        # Output all the symbols except the parentheses.
        elif token == ')':
            top = stack.pop()
            while top != '(':
                postfix.append(top)
                top = stack.pop()

        # Before you can push the operator onto the stack, 
        # you have to pop the stack until you find an operator
        # with a lower priority than the current operator.
        # The popped stack elements are written to output.
        else:
            while stack and (PRECEDENCE[stack[-1]] >= PRECEDENCE[token]):
                postfix.append(stack.pop())
            stack.append(token)

    # After the entire expression is scanned, 
    # pop the rest of the stack 
    # and write the operators in the stack to the output.
    while stack:
        postfix.append(stack.pop())
    return ' '.join(postfix)


# Let's convert infix to postfix

expressions = ['4*2+5*(2+1)/2', '4^2+5*(2+1)/2',  'A*(B+C)/D']

for expr in expressions:
    print(infixToPostfix(expr))