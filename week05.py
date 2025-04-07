#print (1+2)
def is_valid_parentheses(expression:str) -> bool: #type hint new *
    stack = list()
    for letter in expression:
        if letter == "(":
            stack.append(letter)
        if letter == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0

print(is_valid_parentheses("(1+2))"))