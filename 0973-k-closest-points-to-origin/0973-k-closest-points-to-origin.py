class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        out = []
        my_dists = OrderedDict()
        for point in points:
            x = point[0]
            y = point[1]
            
            dist = sqrt(x**2 + y**2)
            
            if dist not in my_dists.keys():
                my_dists[dist] = [point]
            else:
                my_dists[dist].append(point)
        
        count = 0
        for key in sorted(my_dists.keys()):
            for v in my_dists[key]:
                out.append(v)
                count += 1
                if count == k:
                    return out
