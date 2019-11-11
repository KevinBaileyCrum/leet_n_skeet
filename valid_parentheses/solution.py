def isValid(str):
    stack = []
    opening = ['[', '{',  '(']
    closing = [']', '}', ')']
    for char in str:
        if char in opening:
            stack.append(char)
        if char in closing:
            if(len(stack) < 1 or opening.index(stack.pop()) != closing.index(char)):
                return False
    return (len(stack) == 0)

if __name__ == '__main__':
    print(isValid('()'))
    print(isValid(')'))
    print(isValid('('))
    print(isValid('([])'))
    print(isValid('({}[]())'))
    print(isValid('({}[])())'))
