class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        upper_lim = n*2
        total = 0
        lp = 1

        while lp**2 - lp < upper_lim:
            if (n - ( (lp**2 - lp) // 2) ) % lp == 0:
                total += 1
            lp += 1

        return total