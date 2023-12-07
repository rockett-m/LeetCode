class Solution:
    def largestOddNumber(self, num: str) -> str:
        maxx = -1
        for idx, val in enumerate(num):
            if int(val) % 2 == 1:
                maxx = max(maxx, idx)
        
        return '' if maxx == -1 else num[0:maxx+1]