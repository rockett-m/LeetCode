class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        ans = 0
        for i in range(1, n+1):
            ans += (i if i % m != 0 else -i)
        return ans