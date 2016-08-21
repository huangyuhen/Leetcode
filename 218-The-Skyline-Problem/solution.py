class BuildingPoint(object):

    def __init__(self, point, is_start, height):
        self.point = point;
        self.is_start = is_start
        self.height = height
        
    def __lt__(self, other):
        if self.point != other.point:
            return self.point < other.point
        else:
            if self.is_start:
                h1 = -self.height
            else:
                h1 = self.height

            if other.is_start:
                h2 = -other.height;
            else:
                h2 = other.height

            return h1 < h2

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        skyline = []
        i, n = 0, len(buildings)
        liveHR = []
        while i < n or liveHR:
            if not liveHR or i < n and buildings[i][0] <= -liveHR[0][1]:
                x = buildings[i][0]
                while i < n and buildings[i][0] == x:
                    heapq.heappush(liveHR, (-buildings[i][2], -buildings[i][1]))
                    i += 1
            else:
                x = -liveHR[0][1]
                while liveHR and -liveHR[0][1] <= x:
                    heapq.heappop(liveHR)
            height = len(liveHR) and -liveHR[0][0]
            if not skyline or height != skyline[-1][1]:
                skyline += [x, height],
        return skyline