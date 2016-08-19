# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.max = float('-inf')
        
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.compute(root)
        return self.max
        
    def compute(self, root):
        if root is None:
            return 0
        left = max(0, self.compute(root.left))
        right = max(0, self.compute(root.right))
        
        self.max = max(self.max, left + right + root.val)
        return max(left, right) + root.val