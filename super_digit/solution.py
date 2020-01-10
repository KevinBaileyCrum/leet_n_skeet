# non recursive python solution assuming (n, k) -> (int, int)

# given string n (lol i didnt know n was a string when working
# in python) and int k
#   - concatenate n onto iself k times
#   - then sum all digits of concatenated n
#   - until the result is a single digit
#   - resulting in the super digit
#   - superDigit(9875, 2) -> 98759875 -> 58 -> 13 -> 4

def superDigit(n, k):
    concatflag = True
    while n%10 != n:
        accum = 0
        while(n > 0):
            accum += n%10
            n = int(n/10)
        if concatflag:
                accum *= k
                concatflag = False
        n = accum
    return accum

# driver
print(superDigit(9875, 4))
print(superDigit(148, 3))
print(superDigit(48, 3))
