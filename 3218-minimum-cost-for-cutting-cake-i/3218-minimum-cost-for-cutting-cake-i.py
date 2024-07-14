class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        min_cost = 0

        cuts = []
        for h in horizontalCut:
            key = (h, 'horz'); cuts.append(key)
        for v in verticalCut:
            key = (v, 'vert'); cuts.append(key)

        horz, vert = 1, 1
        
        cuts.sort(reverse=True)
        while cuts:
            # pick highest cut first
            cost, dxn = cuts.pop(0)

            if dxn == 'horz':
                min_cost += vert * cost; horz += 1
            elif dxn == 'vert':
                min_cost += horz * cost; vert += 1

        return min_cost