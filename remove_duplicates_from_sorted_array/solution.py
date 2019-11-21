def removeDuplicates(nums):
    while len(nums) > 0:
        curr = nums[-1]
        i = len(nums) - 2
        while i >= 0:
            if nums[i] == curr:
                del nums[i] # it would be better to del the last index here
            else:
                curr = nums[i]
            i -= 1

if __name__ == "__main__":
    a = [0,0,1,1,1,2,2,3,3,4]
    b = [0,1,2,3,4]
    c = [0,1,2,2,3,4]
    d = [1,1,2]
    e = []
    removeDuplicates(a)
    removeDuplicates(b)
    removeDuplicates(c)

    print(a)
    print(b)
    print(c)
    print(d)
