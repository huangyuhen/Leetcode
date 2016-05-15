# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummy = ListNode(0)
        cur = dummy
        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry, val = val / 10, val % 10
            cur.next = ListNode(val)
            cur = cur.next

        if carry == 1:
            cur.next = ListNode(carry)
        return dummy.next
        
#if __name__ == "__main__":
    # a = ListNode(2)
    # b = ListNode(4)
    # c = ListNode(3)
    # d = ListNode(5)
    # e = ListNode(6)
    # f = ListNode(4)

    # i = ListNode(5)
    # k = ListNode(5)
    # a.next, b.next = b, c
    # d.next, e.next = e, f
    # print Solution().addTwoNumbers(i, k)