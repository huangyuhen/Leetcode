# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        max_size = [1]
        def helper(root):
            if root.left is None and root.right is None:
                return 1, root.val, root.val
            left_size, left_min, left_max = 0, root.val, root.val
            if root.left:
                left_size, left_min, left_max = helper(root.left)

            right_size, right_min, right_max = 0, root.val, root.val
            if root.right:
                right_size, right_min, right_max = helper(root.right)

            size = 0
            if (root.left is None or left_size > 0) and (root.right is None or right_size > 0) and left_max <= root.val <= right_min:
                size = left_size + right_size + 1
                max_size[0] = max(max_size[0], size)
            return size, left_min, right_max
        helper(root)
        return max_size[0]