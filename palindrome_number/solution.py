from sys import argv

def isPalindrome(x: int) -> bool:
    False

if __name__ == "__main__":
    with open (argv[1]) as fin:
        for line in fin:
            line = line.strip()
            num, expected = line.split()
            print(line)
            solution = isPalindrome(num)
            if str(solution) == expected:
                print('success')
            else:
                print('failure')
            print("line %s expected %s solution %s\n"%(line, expected, solution))

            print("num is %s expected is %s"%(num, expected))

