# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        def markLeaves(p, l):
            leafs = True
            if p.left and p.left.val != '#':
                leafs = False
                markLeaves(p.left, l)
            if p.right and p.right.val != '#':
                leafs = False
                markLeaves(p.right, l)
            if leafs:
                l.append(p.val)
                p.val = '#'
        
        ret = []
        p = root
        while p and p.val != '#':
            l = []
            markLeaves(p, l)
            ret.append(l)
            p = root
        return ret