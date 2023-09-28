class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # n = abs(n)
        curr = 0
        odd = False
        for i in range(32):
            if i % 2 == 1:
                odd = True
            else:
                odd = False
            
            curr = 2**i
            print(f'{curr = }')
            if curr == n:
                return True
            if curr == abs(n) and odd:
                return False
            elif curr > abs(n):
                return False
        return False
