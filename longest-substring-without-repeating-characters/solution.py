# Kevin Crum
# finds the longest substring without repeating characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# input data from infile presented in a comma seperated list of form
#       string, expected_integer_length_substring

def lengthOfLongestSubstring(s: 'str') -> 'int':
    max_streak = 0
    current_streak = 0
    lookup_set = {}
    beg = 0
    current = 0
    while current < len(s):
        if s[current] in lookup_set:
            if current_streak > max_streak:
                max_streak = current_streak
        else:
            lookup_set[s[current]] = current
            current_streak += 1
        current += 1
    if current_streak > max_streak:
        max_streak = current_streak
    return max_streak

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

