expression = input("Enter an expression: ")
stack = []

for symbol in expression:
    if symbol == '(':
        stack.append('(')
    elif symbol == ')':
        if len(stack) > 0:
            stack.pop()
        else:
            stack.append(')')
            break

if len(stack) == 0:
    print("\nThe expression is correct.")
else:
    print("\nThe expression is incorrect.")