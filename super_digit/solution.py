def superDigit(n, k):
    concatflag = True
    while n%10 != n:
        accum = 0
        while(n > 0):
            accum += n%10
            print()
            print(n%10)
            print(accum)
            print()
            n = int(n/10)
        print('accum')
        if concatflag:
            n = n * k
            concatflag = False
        accum += n
        print(accum)
        print()
        n = accum

    return accum

# driver
superDigit(9875, 4)
