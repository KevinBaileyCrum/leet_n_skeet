# using CTCI one_away (1.5) originally posed as bool if strings are one edit away.
# an edit consists of
# - remove a char
# - add a char
# - replace a char
# note: leetcode hard problem that asks for minium canges required to make chars match

def is_one_away(s1, s2):
    if (max(len(s1), len(s2)) - min(len(s1), len(s2)) <= 1):
        lookUpDict = {}
        for char in s1:
            if char in lookUpDict:
                lookUpDict[char] += 1
            else:
                lookUpDict[char] = 1

        notFoundBuffer = []
        for char in s2:
            if char in lookUpDict:
                lookUpDict[char] -= 1
                if lookUpDict[char] == 0:
                    del lookUpDict[char]
            else:
                notFoundBuffer.append(char)

        # print('len lookUpDict {} len notFoundBuffer {}'.format(len(lookUpDict), len(notFoundBuffer)))
        if len(lookUpDict) == 0 or len(lookUpDict) == 1:
            if len(notFoundBuffer) == 0 or len(notFoundBuffer) == 1:
                return True
    return False

if __name__ == '__main__':
    stringsList = [
        ['pale', 'paleid', False],
        ['pale', 'ple', True],
        ['pales', 'pale', True],
        ['pale', 'pales', True],
        ['pale', 'bale', True],
        ['pale', 'pales', True],
        ['pale', 'bake', False],
        ['pale', 'pale', True],
        ['paleid', 'pale', False]
    ]

    for s1, s2, expected in stringsList:
        if is_one_away(s1, s2) != expected:
            print('error: s1 {} s2 {} expected {}'.format(s1, s2, expected))
        else:
            print('success')
