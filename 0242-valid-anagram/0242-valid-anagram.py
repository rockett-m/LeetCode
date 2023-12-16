class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        marker = True
        a = Counter(sorted(list(s)))
        b = Counter(sorted(list(t)))
        if len(a.values()) != len(b.values()): return False
        for (k,v), (key, val) in zip(a.items(), b.items()):
            if k == key and v == val:
                continue
            else:
                marker = False
                # print(k,v,key,val)
        return marker