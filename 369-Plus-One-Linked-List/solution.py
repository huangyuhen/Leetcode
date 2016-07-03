# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        dummy = ListNode(0)
        while head:
            tmp = head.next
            head.next = dummy.next
            dummy.next = head
            head = tmp
        return dummy.next
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        last = self.reverseList(head)
        tmp = last
        carry = 1
        while last and carry:
            value = last.val + carry
            if value >= 10:
                last.val = value % 10
                carry = 1
            else:
                last.val = value
                carry = 0
            last = last.next
        a = self.reverseList(tmp)
        if carry:
            new = ListNode(1)
            new.next = a
            return new
        return a