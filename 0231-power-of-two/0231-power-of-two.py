class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(32):
            curr = 2**i
            if curr == n:
                return True
            if curr == abs(n) and i % 2 == 1:
                return False
            elif curr > abs(n):
                return False
        return False
