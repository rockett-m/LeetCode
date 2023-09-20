class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        out = s.split('0')
        out = list(filter(None, out))
        return True if len(out) == 1 else False