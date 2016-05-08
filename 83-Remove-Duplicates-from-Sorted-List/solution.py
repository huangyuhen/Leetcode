# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        previous = head
        current = head.next
        while current is not None:
            if previous.val != current.val:
                previous = current
                current = current.next
            else:
                current = current.next
                previous.next = current
        return head
        

# if __name__ == "__main__":
#     a, b, c, d = ListNode(1),ListNode(2),ListNode(3), ListNode(4)
#     a.next, b.next, c.next = b, c, d
#     Solution().deleteDuplicates(a)