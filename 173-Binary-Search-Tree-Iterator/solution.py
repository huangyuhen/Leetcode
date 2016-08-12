# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = collections.deque()
        self.stack1 = collections.deque()
        cur = root
        while cur or self.stack1:
            while cur:
                self.stack1.append(cur)
                cur = cur.left
            cur = self.stack1.pop()
            self.stack.append(cur.val)
            cur = cur.right
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return [False, True][len(self.stack) > 0]

    def next(self):
        """
        :rtype: int
        """
        return self.stack.popleft()

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())