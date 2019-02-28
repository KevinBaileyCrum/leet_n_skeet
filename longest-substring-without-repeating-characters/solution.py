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
    # while current < len(s):

    #     print("beg %s current %s \n current_streak %s max_streak %s"%(beg, current, current_streak, max_streak))
    #     # TODO: must clear from lookup table

    #     if s[current] in lookup_set:
    #         if current_streak > max_streak:
    #             print("inner beg: %s, current: %s"%(beg, current))
    #             max_streak = current_streak
    #         beg = lookup_set[s[current]] + 1
    #         current_streak = current - beg
    #     else:
    #         current_streak += 1
    #     lookup_set[s[current]] = current
    #     current += 1
    # if current_streak > max_streak:
    #     print("outer beg: %s, current: %s"%(beg, current))
    #     max_streak = current_streak
    # return max_streak
    while current < len(s):
        # print("curr-> %s beg %s current %s \n current_streak %s max_streak %s"%(s[current], beg, current, current_streak, max_streak))
        # print(lookup_set)
        if s[current] in lookup_set:
            end_letter = lookup_set[s[current]]
            if current_streak > max_streak:
                max_streak = current_streak
            while beg <= end_letter:
                # print(lookup_set[s[current]])
                # print("deleting %s"%(lookup_set[s[beg]]))
                del lookup_set[s[beg]]
                beg += 1
                current_streak -= 1
        lookup_set[s[current]] = current
        current_streak += 1
        # print("lookup_set[s[current]]"%(lookup_set[s[current]]))
        #print(lookup_set[s[current]])
        #print(s[current])
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

