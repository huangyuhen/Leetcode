class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        high = 0
        container = [0 for _ in xrange(len(height))]

        for i in xrange(len(container)):
            container[i] = high
            high = max(high, height[i])

        high = 0
        res = 0
        for i in xrange(len(height) - 1, 0, -1):
            container[i] = min(high, container[i])
            high = max(high, height[i])
            res += [0, container[i] - height[i]][container[i] - height[i] > 0];
        return res