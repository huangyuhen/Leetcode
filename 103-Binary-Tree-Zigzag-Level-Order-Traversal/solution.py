# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result, cur, nextLevel, odd, curList = [],1, 0, 1, []
        if root is None:
            return result
        
        stack = collections.deque()
        stack.append(root)

        while stack:
            node = stack.pop()
            cur -= 1
            if odd:
                curList.append(node.val)
            else:
                curList.insert(0, node.val)

            if node.left:
                nextLevel += 1
                stack.appendleft(node.left)

            if node.right:
                nextLevel += 1
                stack.appendleft(node.right)

            if cur == 0:
                result.append(curList)
                odd = [1, 0][odd == 1]
                curList = []
                cur, nextLevel = nextLevel, 0

        return result
        