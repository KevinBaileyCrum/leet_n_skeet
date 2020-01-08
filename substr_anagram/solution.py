# Python3 program to print all possible
# substrings of a given string

# Function to print all sub strings
def subString(s):
    substrList = []
    i = 0
    substrList.append(s)
    while i < len(s):
        j=i+1
        while j < len(s):
            substrList.append(s[i:j])
            j+=1
        i+=1
    return substrList

# Driver program to test above function
s = 'abcd'
print(subString(s))

