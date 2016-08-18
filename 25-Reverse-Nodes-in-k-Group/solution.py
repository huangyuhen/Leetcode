# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def __init__(self):
        self.result = None
        self.check = 1
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if k < 2 or head is None or head.next is None:
            return head
        i, dummyHead = 0, ListNode(-1)
        dummyHead.next = head
        begin = dummyHead
        self.result = head
        while head:
            i += 1
            if i % k == 0:
                begin = self.reverseNode(begin, head.next)
                head = begin.next
            else:
                head = head.next
        return self.result


    def reverseNode(self, start, end):
        dummy, head = ListNode(-1), start.next
        first = head
        while head != end:
            dummy.next, head.next, head = head, dummy.next, head.next
        first.next = head
        start.next = dummy.next
        if self.result != dummy.next and self.check == 1:
            self.result = dummy.next
            self.check = 0

        return first