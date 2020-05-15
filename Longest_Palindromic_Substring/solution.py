def getPalindromeLength(s: str) -> int:
    start = 0
    end = len(s) - 1

    while start < end:
        print(f'start: {start} end {end} s[start] {s[start]} s[end] {s[end]}')
        if s[start] != s[end]:
            return (0, '')
        start += 1
        end   -= 1

    return (len(s), s)

def longestPalindrome(s: str) -> str:
    print(s)
    # iterate through every substring
    max = (0, '')
    i = 0
    while i < len(s):
        j = i
        while j < len(s):
            print({s[i:j+1]})
            # determine length of palindrome in substring
            # print(palindromeLength(s[i:j+1]))
            palindromeLength = getPalindromeLength(s[i:j+1])
            # update max
            if palindromeLength[0] > max[0]:
                max = palindromeLength
            j += 1
        i += 1

    return max[1]

if __name__ == "__main__":
    with open ('infile.in') as fin:
        for line in fin:
            string, expected = line.split(',')
            expected = expected.strip()
            solution = longestPalindrome(string)
            if solution == expected.strip():
                print('success')
            else:
                print('failure\n   %s'%(string))
            print('\texpected: %s\n\tsolution: %s'%(expected, solution))
