class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = 0
        i = 1
        while n >= i:
            n -= i
            i += 1
            k += 1

        return k