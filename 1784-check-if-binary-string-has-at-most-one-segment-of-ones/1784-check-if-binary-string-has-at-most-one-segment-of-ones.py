class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        out = s.split('0')
        return True if len(list(filter(None, out))) == 1 else False