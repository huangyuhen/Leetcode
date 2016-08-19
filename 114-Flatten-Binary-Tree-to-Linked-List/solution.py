# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.stack = collections.deque()

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.preorder(root)
        prev = self.stack.popleft()
        while self.stack:
            prev.left = None
            prev.right = self.stack.popleft()
            prev = prev.right


    def preorder(self, root):
        if root:
            self.stack.append(root)
            self.preorder(root.left)
            self.preorder(root.right)