# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.helper(root, res, 0)
        return res

    def helper(self, root, res, depth):
        if root:
            if len(res) == depth:
                res.append(root.val)
            self.helper(root.right, res, depth + 1)
            self.helper(root.left, res, depth + 1)