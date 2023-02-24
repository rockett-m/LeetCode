from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = Counter(t) - Counter(s)
        for k,v in res.items():
            if v == 1:
                return k
        return -1