class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1: return [0]
        half = n // 2
        out = [-x for x in range(1, half+1)] + [x for x in range(1, half+1)]
        
        return out if n % 2 == 0 else out + [0]
