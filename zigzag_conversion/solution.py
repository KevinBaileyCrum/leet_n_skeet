def zigzagConversion(s, numRows):
    if numRows == 1:
        return s
    currentRow = 0
    goingDown = False
    zagMatrix = [[] for _ in range(min(numRows, len(s)))]
    for char in s:
        zagMatrix[currentRow].append(char)
        if currentRow == 0 or currentRow == numRows - 1:
            goingDown = not(goingDown)
        if goingDown:
            currentRow += 1
        else:
            currentRow -= 1
    solution = ''
    for row in zagMatrix:
        for char in row:
            solution += (char)
    return solution

if __name__ == '__main__':
    zigzagConversion('paypalishiring', 3)
