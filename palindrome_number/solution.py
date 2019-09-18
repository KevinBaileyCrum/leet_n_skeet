from sys import argv
import math

def isPalindrome(x: int) -> bool:
    while(x > 0):
        power = int(math.log10(x))
        i=0
        while i<=math.ceil(power/2):
            if int( x / 10 ** (power - i*2) ) == x % 10:
                x = x % 10 ** (power - (i*2))
                x = int(x/10)
                i += 1
            else:
                return False
        return True
    if x == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    with open (argv[1]) as fin:
        for line in fin:
            line = line.strip()
            num, expected = line.split()
            print('\n')
            print(line)
            solution = isPalindrome(int(num))
            if str(solution) == expected:
                print('success')
            else:
                print('failure')

