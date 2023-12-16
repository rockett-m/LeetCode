class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = Counter(sorted(list(s)))
        b = Counter(sorted(list(t)))
        if len(a.values()) != len(b.values()): return False
        for (k,v), (key, val) in zip(a.items(), b.items()):
            if k == key and v == val:
                continue
            else:
                return False
        return True