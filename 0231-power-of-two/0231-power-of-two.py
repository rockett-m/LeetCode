class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(32):
            if 2**i == n:
                return True
            if 2**i == abs(n) and i % 2 == 1:
                return False
            elif 2**i > abs(n):
                return False
        return False
