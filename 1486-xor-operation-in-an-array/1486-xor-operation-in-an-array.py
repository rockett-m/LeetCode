class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        total = 0

        for i in range(n):
            num = start + 2 * i
            total ^= num

        return total