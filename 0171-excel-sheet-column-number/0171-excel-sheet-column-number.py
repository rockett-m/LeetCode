class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 0        
        for idx, val in enumerate(reversed(columnTitle)):
            num += (ord(val) - 64) * pow(26, idx)
        return num
