# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import Queue

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        queue = Queue.Queue()
        curLevel = 1
        nextLevel = 0
        minValue = sys.maxint
        queue.put(root)
        while not queue.empty():
            node = queue.get()
            minValue = [minValue, node.val][abs(target - float(node.val)) < abs(target - float(minValue))]
            curLevel -= 1
            if node.left is not None:
                queue.put(node.left)
                nextLevel += 1
            if node.right is not None:
                queue.put(node.right)
                nextLevel += 1
            if curLevel == 0:
                curLevel = nextLevel
                nextLevel = 0
        return minValue
        
        