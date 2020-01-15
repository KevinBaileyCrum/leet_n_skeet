# 1.4:  Given a string, determine if it is a permuation of a palindrome
# assumed spaces didnt matter here

def isPalindromePermutation(string):
    lookUpDict = {}
    charCount = 0
    for char in string:
        if char.isalpha():
            charCount += 1
            if char not in lookUpDict:
                lookUpDict[char] = 1
            else:
                lookUpDict[char] += 1

    oddOneOut = 0
    for key in lookUpDict.keys():
        if lookUpDict[key] % 2 != 0:
            oddOneOut += 1

    if charCount % 2 == 0 and oddOneOut == 0:
        return True
    elif charCount % 2 == 1 and oddOneOut == 1:
        return True
    return False

if __name__ == '__main__':
    stringObjs = [
        ['taco cat', True],
        ['racecar', True],
        ['aatt cco', True],
        ['kfjad kfej', False],
        ['t a c o a t c', True]
    ]

    for string, truthiness in stringObjs:
        if isPalindromePermutation(string) == truthiness:
            print('success')
        else:
            print('error: string: {} expected {} returned {}'.format(string, truthiness, isPalindromePermutation(string)))
