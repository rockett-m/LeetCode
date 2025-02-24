class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        if len(s) <= 1: return True

        c = Counter(s)
        return True if len(set(c.values())) == 1 else False