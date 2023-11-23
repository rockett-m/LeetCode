class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        maxarea = 0
        pts = sorted([x[0] for x in points])
        for idx, x in enumerate(pts):
            if idx == 0: continue
            diff = pts[idx] - pts[idx-1]
            if diff > maxarea: maxarea = diff
        return maxarea
