# Evaluate Reverse Polish Notation
# Difficulty: Medium
# Topic: Stack
# Time: O(n) | Space: O(n)
#
# Approach:
# Utilize a stack to evaluate the expression. Traverse each token: if it's a number, push it onto the stack; if it's an operator, pop the top two elements, perform the operation, and push the result back onto the stack.
#
# Solution:

def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token in '+-*/':
            b, a = stack.pop(), stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))  # for correct division round
        else:
            stack.append(int(token))
    return stack[0]
