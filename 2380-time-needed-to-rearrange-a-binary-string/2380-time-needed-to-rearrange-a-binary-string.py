class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        total = 0
        while s.count("01") > 0:
            total += 1
            s = s.replace("01", "10")
        return total