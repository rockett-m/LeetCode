class Solution:

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = [[None]*len(row) for row in triangle]

        def dp(ridx, cidx) -> int:
            # end case
            if ridx >= len(triangle)-1:
                # child node val
                # memo[ridx][cidx] = triangle[ridx][cidx]
                # print(memo)
                return triangle[ridx][cidx]

            # so we compute opt path once and only once
            if memo[ridx][cidx] is None:

                memo[ridx][cidx] = min(
                    dp(ridx+1, cidx),  # child 0
                    dp(ridx+1, cidx+1) # child 1
                ) + \
                triangle[ridx][cidx] # parent
        
            return memo[ridx][cidx]

        return dp(0, 0)