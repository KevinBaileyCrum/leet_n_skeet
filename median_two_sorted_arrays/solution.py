from sys import argv

def findMedianSortedArrays(nums1, nums2):
    half_iteratoins = (len(nums1) + len(num2)) / 2
    p1 = 0
    p2 = 0
    num_iterations = 0
    # while num_iterations < half_iteratoins:
    print("top")
    while p1 < len(nums1) and p2 < len(num2):
        print('inner both')
        if num_iterations < half_iteratoins:
            if nums1[p1] < nums2[p2]:
               p1 += 1
            else:
               p2 += 1
        else:
            return 2.5

    while p1 < len(nums1):
        print('inner 1')
        if num_iterations < half_iteratoins:
            # optimization extrapolate median here
            p1 += 1
        else:
            return nums1[p1]
    while p2 < len(nums2):
        print('inner 2')
        if  num_iterations < half_iteratoins:
            p2 += 1
        else:
            return nums2[p2]
    return -1



if __name__ == "__main__":
    with open (argv[1]) as fin:
        for line in fin:
            line = line.strip()
            num1, num2, expected = line.split(',')
            num1 = num1.split()
            num2 = num2.split()
            expected = expected.strip()
            solution = findMedianSortedArrays(num1, num2)
            if str(solution) == expected:
                print('success')
            else:
                print('failure')
            print("line %s expected %s solution %s"%(line, expected, solution))

