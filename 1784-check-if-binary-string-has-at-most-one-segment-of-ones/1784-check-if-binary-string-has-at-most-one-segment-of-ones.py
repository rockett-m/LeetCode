class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return True if len(list(filter(None, s.split('0')))) == 1 else False