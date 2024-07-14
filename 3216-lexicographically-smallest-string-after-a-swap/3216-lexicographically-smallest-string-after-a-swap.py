class Solution:
    def getSmallestString(self, s: str) -> str:
        if list(s) == sorted(s): return s

        ans = [ int(x) for x in s ]

        for i in range(1, len(s)):

            if ans[i] % 2 == 0 and ans[i-1] % 2 == 0:
                if ans[i] < ans[i-1]:
                    evens = True
                    ans[i-1], ans[i] = ans[i], ans[i-1]
                    break

            if ans[i] % 2 == 1 and ans[i-1] % 2 == 1:
                if ans[i] < ans[i-1]:
                    odds = True
                    ans[i-1], ans[i] = ans[i], ans[i-1]
                    break

        x = [str(x) for x in ans]

        return ''.join(x)