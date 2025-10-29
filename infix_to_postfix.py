def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []
    
    for char in expression.replace(" ", ""):
        if char.isalnum():
            output.append(char)
        elif char in precedence:
            while stack and stack[-1] != '(' and (
                precedence[char] < precedence.get(stack[-1], 0) or
                (precedence[char] == precedence.get(stack[-1], 0) and char != '^')
            ):
                output.append(stack.pop())
            stack.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack:
                stack.pop()
    
    while stack:
        output.append(stack.pop())
    
    return ' '.join(output)