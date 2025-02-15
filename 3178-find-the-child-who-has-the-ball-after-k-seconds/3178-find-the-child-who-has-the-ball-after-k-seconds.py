class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        start, end = 0, n-1

        full = k // (n-1)
        partial = k % (n-1)

        # passing to the right
        if full % 2 == 0:
            return partial
        else:
            return end - partial
