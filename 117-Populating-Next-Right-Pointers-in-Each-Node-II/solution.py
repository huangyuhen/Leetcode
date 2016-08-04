# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        
        prev, head, cur = None, None, root
        while cur is not None:
            while cur is not None:
                if cur.left is not None:
                    if prev is not None:
                        prev.next = cur.left
                    else:
                        head = cur.left
                    prev = cur.left
                if cur.right is not None:
                    if prev is not None:
                        prev.next = cur.right
                    else:
                        head = cur.right
                    prev = cur.right
                cur = cur.next
            prev, head, cur = None, None, head