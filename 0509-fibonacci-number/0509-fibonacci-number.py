class Solution:
    def fib(self, n: int) -> int:
        # 0 1 2 3 4 5 6 7
        # 0 1 1 2 3 5 8 13

        if n < 2:
            return n

        sum = 0
        prev = [0, 1]

        for i in range(n+1):
            if i >= 2:    
                sum = prev[0] + prev[1]

                prev[0] = prev[1]
                prev[1] = sum

        return sum