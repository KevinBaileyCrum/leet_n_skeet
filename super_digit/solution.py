# non recursive python solution assuming (n, k) -> (int, int)

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
