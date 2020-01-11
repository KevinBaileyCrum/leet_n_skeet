#algorithm that determines if a string has all unique char

def isUnique(string):
    lookUp = set()
    for char in string:
        if char not in lookUp:
            lookUp.add(char)
        else:
            return False
    return True

if __name__ == '__main__':
    stringList = [
        ['ancd', True],
        ['abcdefghijklmnopqrstuv', True],
        ['abba', False]
    ]

    for string, expected in stringList:
        if isUnique(string) != expected:
            print('error: string={} expected={}'.format(string, expected))

