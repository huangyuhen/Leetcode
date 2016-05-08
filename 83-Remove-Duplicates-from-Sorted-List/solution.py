# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeDup(self, head):
        if head is None or head.next is None:
            return head
        if head.val == head.next.val:
            head.next = head.next.next
            return self.deleteDuplicates(head)
        else:
            head.next = self.deleteDuplicates(head.next)
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        self.removeDup(head)
        return head
        

# if __name__ == "__main__":
#     a, b, c, d = ListNode(1),ListNode(2),ListNode(3), ListNode(4)
#     a.next, b.next, c.next = b, c, d
#     Solution().deleteDuplicates(a)