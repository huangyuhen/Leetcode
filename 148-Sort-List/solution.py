# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        if head is None or head.next is None:
            return head
        prev, slow, fast = None, head, head
        while fast is not None and fast.next is not None:
            prev, slow, fast = slow, slow.next, fast.next.next
        prev.next = None

        sorted_l1 = self.sortList(head)
        sorted_l2 = self.sortList(slow)

        return self.mergeTwoLists(sorted_l1, sorted_l2)

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next, cur, l1 = l1, l1, l1.next
            else:
                cur.next, cur, l2 = l2, l2, l2.next
        if l1 is not None:
            cur.next = l1
        elif l2 is not None:
            cur.next = l2
        return dummy.next
        