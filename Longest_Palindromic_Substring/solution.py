def longestPalindrome(s: str) -> str:
    return "test"

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
