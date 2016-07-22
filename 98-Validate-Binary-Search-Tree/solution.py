# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBSTcheck(self, root, low, high):
        if root is None:
            return True
        return low < root.val and high > root.val and self.isBSTcheck(root.left, low, root.val) and self.isBSTcheck(root.right, root.val, high)
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isBSTcheck(root, float("-inf"), float("inf"))