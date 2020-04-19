# implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:

# What should we return when needle is an empty string? This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(needle) > len(haystack):
            return -1
        windex = 0 # window starting index
        while (len(needle) + windex <= len(haystack)):
            if haystack[windex:len(needle)+windex] == needle:
                return windex
            windex += 1
        return -1


# I feel this can be improved by writing my own comapre function (line 27)
# with my own compare I can find the index of where the mismatch occured
# and decide how far to slide my window as opposed to sliding by one
# each iteration
