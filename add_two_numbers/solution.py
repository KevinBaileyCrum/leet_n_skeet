# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        sumList = ListNode()
        current = sumList
        while (l1 or l2):
            # cases for nodes in lists
            if (l1 and l2):
                sum = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif (l1 and not l2):
                sum = l1.val + carry
                l1 = l1.next
            elif (l2 and not l1):
                sum = l2.val + carry
                l2 = l2.next
            # handle carry
            carry = 0
            if (sum >= 10):
                carry = int(sum / 10)
                sum = sum % 10
            # append to list
            print(sum)
            current.next = ListNode(sum)
            current = current.next
        # carry at end
        if carry:
            current.next = ListNode(carry)
        return sumList.next
