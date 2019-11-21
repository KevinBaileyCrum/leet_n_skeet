def removeDuplicates(nums):
    curr = nums.pop()
    i = len(nums) - 1
    while i > 0:
        if nums[i] == curr:
            del nums[i]
        else:
            curr = nums[i]
        i -= 1

if __name__ == "__main__":
    a = [0,0,1,1,1,2,2,3,3,4]
    b = [0,1,2,3,4]
    c = [0,1,2,2,3,4]
    removeDuplicates(a)
    removeDuplicates(b)
    removeDuplicates(c)

    print(a)
    print(b)
    print(c)
