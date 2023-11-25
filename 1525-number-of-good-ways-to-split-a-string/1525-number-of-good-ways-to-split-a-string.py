class Solution:
    def numSplits(self, s: str) -> int:
        total = 0
        lset = set()
        rcounts = Counter(s)
        for idx, val in enumerate(s):
            
            if idx == 0:
                lset.add(val)
                rcounts[val] -= 1
                if rcounts[val] == 0: del rcounts[val]
                continue

            if len(lset) == len(rcounts.keys()): total += 1
                
            lset.add(val)
            rcounts[val] -= 1
            if rcounts[val] == 0: del rcounts[val]

        return total
