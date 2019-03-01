from sys import argv

def findMedianSortedArrays(nums1, nums2):
    half_iteratoins = (len(nums1) + len(num2)) / 2
    p1 = 0
    p2 = 0
    num_iterations = 0
    while num_iterations < half_iteratoins:
        while p1 < len(nums1) and p2 < len(num2) and num_iterations < half_iteratoins:
            if nums1[p1] < nums2[p2]:
               print("i am the wind")


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

