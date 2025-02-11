class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:

        while part in s:
            spl = s.split(part)
            s = spl.pop(0) + part.join(spl)
        return s
