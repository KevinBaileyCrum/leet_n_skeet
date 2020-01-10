# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

from math import inf

def maxSubArray(nums):
    maxSum = -inf
    curSum = -inf

    for num in nums:
        curSum = max(num, curSum + num)
        maxSum = max(curSum, maxSum)
    return maxSum

if __name__ == '__main__':
    intList = [-2,1,-3,4,-1,2,1,-5,4]
    maxSubArray(intList)
