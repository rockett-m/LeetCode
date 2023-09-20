class Solution:
    def secondHighest(self, s: str) -> int:
        out = set()
        for x in s:
            if x.isdigit():
                out.add(int(x))
        
        return -1 if len(out) < 2 else sorted(out)[-2]
