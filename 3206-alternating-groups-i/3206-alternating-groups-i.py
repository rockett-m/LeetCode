class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        count = 0
        ln = len(colors)
        if ln < 3: return count
        
        for i in range(ln):
            if colors[i] != colors[(i-1) % ln] and \
               colors[i] != colors[(i+1) % ln]:
                count += 1
        return count
