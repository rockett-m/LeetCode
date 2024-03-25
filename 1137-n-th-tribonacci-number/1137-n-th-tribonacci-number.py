class Solution:
    def tribonacci(self, n: int) -> int:
        self.n = n
        prev = [0, 1, 1]
        if n < 3:
            return prev[n]
        return self.recurse(3, prev)[-1]

    def recurse(self, num: int, prev: list):

        prev.append(sum(prev))
        prev.pop(0)

        if self.n - num == 0:
            return prev
        else:
            self.recurse(num+1, prev)
            return prev
