class Solution:
    def countSegments(self, s: str) -> int:
        if len(s) == 0:
            return 0

        ss = s.split(' ')

        return sum([1 for x in range(len(ss)) if ss[x] != ''])