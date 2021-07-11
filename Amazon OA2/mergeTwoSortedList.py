# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0,None)
        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        if l1:
            dummy.next = l1
        else:
            dummy.next = l2
        return dummy.next
ss = Solution()
n2=ListNode(5,None)
n3 = ListNode(6,None)
l1=ListNode(2,n2)

l2=ListNode(3,n3)
print(ss.mergeTwoLists(l1,l2))
