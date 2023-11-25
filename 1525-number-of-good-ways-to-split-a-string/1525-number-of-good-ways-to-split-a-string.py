class Solution:
    def numSplits(self, s: str) -> int:
        num = 0
        lset = set()
        right = Counter(s)
        for idx, val in enumerate(s):
            
            if idx == 0:
                lset.add(val)
                right[val] -= 1
                if right[val] == 0:
                    del right[val]
                continue

            if len(lset) == len(right.keys()):
                num += 1
            lset.add(val)
            right[val] -= 1
            if right[val] == 0:
                del right[val]
        return num
