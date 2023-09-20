class Solution:
    def secondHighest(self, s: str) -> int:
        out = set()
        for x in s:
            if x.isdigit():
                out.add(int(x))
        if len(out) < 2:
            return -1
        else:
            return sorted(out)[-2]