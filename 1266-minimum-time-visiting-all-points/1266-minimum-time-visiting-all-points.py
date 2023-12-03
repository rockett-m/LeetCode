class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for idx, point in enumerate(points):
            if idx == 0:
                continue

            prev = points[idx-1]
            xdelta = abs(point[0] - prev[0])
            ydelta = abs(point[1] - prev[1])

            if xdelta > 0 and ydelta == 0: # horz is fastest and only way
                time += xdelta
            elif ydelta > 0 and xdelta == 0: # vert is fastest and only way
                time += ydelta
            else:                
                zdelta = xdelta - ydelta
                time += abs(zdelta) # diag

                if zdelta <= 0: # (x < y) go vertical
                    time += xdelta
                elif zdelta > 0: # (x > y) go sideways
                    time += ydelta

        return time