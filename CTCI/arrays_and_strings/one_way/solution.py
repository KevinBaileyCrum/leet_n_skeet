# using CTCI one_away (1.5) originally posed as bool if strings are one edit away.
# an edit consists of
# - remove a char
# - add a char
# - replace a char
# note: leetcode hard problem that asks for minium canges required to make chars match

def is_one_away(s1, s2):
    if (max(len(s1), len(s2)) - min(len(s1), len(s2)) <= 1):
        print('hello')
    return False

if __name__ == '__main__':
    stringsList = [
        ['pale', 'paleid', False],
        ['pale', 'ple', True],
        ['pales', 'pale', True],
        ['pale', 'bale', True],
        ['pale', 'bake', False],
        ['pale', 'pale', False]
    ]

    for s1, s2, expected in stringsList:
        if is_one_away(s1, s2) != expected:
            print('error: s1 {} s2 {} expected {}'.format(s1, s2, expected))
        else:
            print('success')
