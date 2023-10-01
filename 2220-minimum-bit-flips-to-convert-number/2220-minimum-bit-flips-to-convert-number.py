class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        s = bin(start).split('0b')[1]
        e = bin(goal).split('0b')[1]
        print(s, e)
        if len(e) > len(s):
            s = (len(e) - len(s)) * '0' + s
        elif len(s) > len(e):
            e = (len(s) - len(e)) * '0' + e

        count = 0
        for idx, val in enumerate(s):
            if val != e[idx]:
                count += 1
        return count