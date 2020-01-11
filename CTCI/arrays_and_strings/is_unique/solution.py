#algorithm that determines if a string has all unique char

# with additional data stuctures
def isUnique(string):
    lookUp = set()
    for char in string:
        if char not in lookUp:
            lookUp.add(char)
        else:
            return False
    return True

# without additional data stuctures
def isUniqueRaw(string):
    s = sorted(string)
    prev = string[0]
    for i in range(1, len(s)):
        if string[i] == prev:
            return False
        prev = string[i]
    return True

if __name__ == '__main__':
    stringList = [
        ['ancd', True],
        ['abcdefghijklmnopqrstuv', True],
        ['abba', False]
    ]

    for string, expected in stringList:
        if isUnique(string) != expected:
            print('isUnique error: string={} expected={}'.format(string, expected))
        if isUniqueRaw(string) != expected:
            print('isUniqueRaw error: string={} expected={}'.format(string, expected))
