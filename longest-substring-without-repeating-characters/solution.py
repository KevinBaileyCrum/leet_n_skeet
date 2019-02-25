# finds the longest substring without repeating characters

def lengthOfLongestSubstring(s: 'str') -> 'int':
    max = 0
    count = 0
    lookup_set = set()
    for char in s:
        if char in lookup_set:
            if count > max:
                max = count
            lookup_set.clear()
            count = 0
        lookup_set.add(char)
        count += 1

    if count > max:
        return count
    return max


if __name__ == "__main__":
    with open ('infile.in') as fin:
        for line in fin:
            string, expected = line.split(',')
            expected = expected.strip()
            solution = lengthOfLongestSubstring(string)
            if solution == int(expected.strip()):
                print('success')
            else:
                print('failure\n   %s'%(string))
            print('\texpected: %s\n\tsolution: %s'%(expected, solution))

