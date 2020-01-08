# Python3 program to print all possible
# substrings of a given string
import string

# Function to print all sub strings
def subString(s):
    substrList = []
    count = 0
    for i in range(len(s)):
        j=i+1
        while j <= len(s):
            count += 1
            substrList.append((count, s[i:j]))
            j+=1
        i+=1
    return substrList

# Driver program to test above function
s0 = 'abcd'
s1 = 'mom'
s2 = string.ascii_lowercase
s3 = 'z'
print(subString(s1))


