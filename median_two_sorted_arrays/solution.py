from sys import argv

def get_next(nums1, p1, nums2, p2):
    less_than = -1
    if p1 < len(nums1) and p2 < len(nums2):
        if nums1[p1] < nums2[p2]:
            less_than = nums1[p1]
            p1 += 1
        else:
            less_than = nums2[p2]
            p2 += 1
    elif p1 < len(nums1):
        less_than = nums1[p1]
        p1 += 1
    elif p2 < len(nums2):
        less_than = nums2[p2]
        p2 += 1
    return float(less_than), p1, p2

def findMedianSortedArrays(nums1, nums2):
    half_iterations = ((len(nums1) + len(nums2)) / 2)
    is_even = (len(nums1) + len(nums2)) % 2 == 0
    p1 = 0
    p2 = 0
    while p1 + p2 < half_iterations:
        curr, p1, p2 = get_next(nums1, p1, nums2, p2)
    if is_even:
        curr_next, p1, p2 = get_next(nums1, p1, nums2, p2)
        curr = (curr_next + curr) / 2
    return curr

if __name__ == "__main__":
    with open (argv[1]) as fin:
        for line in fin:
            line = line.strip()
            num1, num2, expected = line.split(',')
            num1 = num1.split()
            num2 = num2.split()
            expected = expected.strip()
            print(line)
            solution = findMedianSortedArrays(num1, num2)
            if str(solution) == expected:
                print('success')
            else:
                print('failure')
            print("line %s expected %s solution %s\n"%(line, expected, solution))

