class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        @lru_cache(maxsize=None)
        def dp(xStart: int, yStart: int, movesLeft: int) -> int:
            # base cases
            if not (0 <= xStart < m and 0 <= yStart < n): return 1

            if movesLeft <= 0: return 0

            paths = 0
            for (x, y) in [ (-1,0), (1,0), (0,1), (0,-1) ]:
                paths += dp(xStart + x, yStart + y, movesLeft-1)
                paths %= (10**9 + 7)

            return paths 

        return dp(startRow, startColumn, maxMove) 
