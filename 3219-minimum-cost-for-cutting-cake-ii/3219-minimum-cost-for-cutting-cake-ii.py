class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        min_cost = 0

        cuts = []
        for h in horizontalCut:
            key = (-h, 'h'); cuts.append(key)
        for v in verticalCut:
            key = (-v, 'v'); cuts.append(key)

        horz, vert = 1, 1
        # max heap with neg weights
        heapify(cuts)
        while cuts:
            # highest cut avail
            cost, dxn = heappop(cuts)
            # turn neg weight pos
            cost *= -1

            if dxn == 'h':
                min_cost += vert * cost; horz += 1
            elif dxn == 'v':
                min_cost += horz * cost; vert += 1

        return min_cost