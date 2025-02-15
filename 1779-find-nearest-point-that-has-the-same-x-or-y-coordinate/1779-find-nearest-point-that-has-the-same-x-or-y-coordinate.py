class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        # (lowest index, abs diff best)
        ans = (-1, 1e6)

        for idx, point in enumerate(points):
            xp, yp = point
            # can't beat the same point with abs dist of 0,0
            if x == xp and y == yp:
                return idx
            # compare vs prev best (update only if md is lower)
            elif x == xp or y == yp:
                md = abs(xp - x) + abs(yp - y)
                if md < ans[1]:
                    ans = (idx, md)
            # need x or y on same plane as point's x and/or y

        return ans[0]