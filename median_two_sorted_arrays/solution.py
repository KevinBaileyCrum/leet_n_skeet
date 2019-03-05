from sys import argv

# def return_min(nums1=None, nums2=None,p1=None, p2=None):
#     if p1 is not None and p2 is not None:
#         if nums1[p1] < nums2[p2]:
#             avg1 = nums1[p1]
#             p1 += 1
#         else:
#             avg1 = nums2[p2]
#             p2 += 1
#         if nums1[p1] < nums2[p2]:
#             avg2 = nums1[p1]
#         else:
#             avg2 = nums2[p2]
#     elif p1 is not None and p2 is None:
#         avg1 = nums1[p1]
#         avg2 = nums1[p1+1]
#     else:
#         avg1 = nums2[p2]
#         avg2 = nums2[p2+1]
#     return (avg1 + avg2) / 2


# def findMedianSortedArrays(nums1, nums2):
#     half_iteratoins = ((len(nums1) + len(nums2)) / 2) - 1
#     is_even = (len(nums1) + len(nums2)) % 2 == 0
#     p1 = 0
#     p2 = 0
#     print("top")
#     while p1 < len(nums1) and p2 < len(num2):
#         print('inner both')
#         if p1 + p2 < half_iteratoins:
#             if nums1[p1] < nums2[p2]:
#                p1 += 1
#             else:
#                p2 += 1
#         elif not is_even:
#             if nums1[p1] < nums2[p2]:
#                 return nums1[p1]
#             else:
#                 return nums2[p2]
#         else:
#             return_min(nums1, nums2, p1, p2)
#     while p1 < len(nums1):
#         print('inner 1')
#         if p1 + p2 < half_iteratoins:
#             # optimization extrapolate median here
#             p1 += 1
#         elif not is_even:
#             return nums1[p1]
#         else:
#             return return_min(nums1, None, p1, None)
#     while p2 < len(nums2):
#         print('inner 2')
#         if  p1 + p2 < half_iteratoins:
#             p2 += 1
#         elif not is_even:
#             return nums2[p2]
#         else:
#             return return_min(None, nums2, None, p2)
#     return -1

def get_next(nums1, p1, nums2, p2):
    less_than = -1
    if p1 < len(nums1) and p2 < len(nums2):
        if nums1[p1] < nums2[p2]:
            less_than = nums1[p1]
            p1 += 1
    elif p1 < len(nums1):
        less_than = nums1[p1]
        p1 += 1
    elif p2 < len(nums2):
        less_than = nums2[p2]
        p2 += 1
    print("returning p1 %s, p2 %s"%(p1, p2))
    return less_than

def findMedianSortedArrays(nums1, nums2):
    half_iterations = ((len(nums1) + len(nums2)) / 2) -1
    is_even = (len(nums1) + len(nums2)) % 2 == 0
    p1 = 0
    p2 = 0
    while p1 + p2 < half_iterations:
        print("before p1 %s, p2 %s"%(p1, p2))
        curr = get_next(nums1, p1, nums2, p2)
        print("after p1 %s, p2 %s"%(p1, p2))
    if is_even:
        curr_next = get_next(nums1, p1, nums2, p2)
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
            solution = findMedianSortedArrays(num1, num2)
            if str(solution) == expected:
                print('success')
            else:
                print('failure')
            print("line %s expected %s solution %s"%(line, expected, solution))

