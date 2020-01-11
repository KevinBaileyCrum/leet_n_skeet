# given two strings determine if one is a permutation of the other

# o(s1) to load in dict
#
def checkPermutations(s1, s2):
    loopUpDict = {}

    for char in s1:
        if char not in loopUpDict:
            loopUpDict[char] = 1
        else:
            loopUpDict[char] += 1
    for char in s2:
        if char in loopUpDict:
            if loopUpDict[char] > 1:
                loopUpDict[char] -= 1
            else:
                del loopUpDict[char]
        else:
            return False

    return not loopUpDict # empty dict eval to False

if __name__ == '__main__':
    a = 'abbc'
    b = 'acbb'

    c = ''
    d = 'a'

    e = ';lfdfjhadfajdfdhfdfg'
    f = '123'

    print(checkPermutations(a,b))
    print(checkPermutations(c,d))
    print(checkPermutations(d,c))
    print(checkPermutations(c,c))
    print(checkPermutations(e,f))
