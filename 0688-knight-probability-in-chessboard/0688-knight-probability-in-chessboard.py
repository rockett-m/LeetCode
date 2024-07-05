class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        memo = {}
        moves = [(2,1),  (2,-1),
                (1,-2),  (-1,-2),
                (-2,-1), (-2,1),
                (-1,2),  (1,2) ]

        def in_bounds(row: int, column: int) -> bool:
            if min(row, column) >= 0 and max(row, column) < n:
                return True
            return False
        
        def dp(start_row: int, start_col: int, moves_remaining: int) -> float:
            # any 8 moves from here are all invalid, no need to expand
            if not in_bounds(start_row, start_col): return 0
            
            # in bounds and no moves left - knight on board - success
            if moves_remaining == 0: return 1

            # if found in table return prob - don't repeat exact r, c, k
            if (start_row, start_col, moves_remaining) in memo.keys():
                return memo[(start_row, start_col, moves_remaining)]

            # future probability for each of the 8 moves - cond prob
            prob_still_on = 0.0
            for (side_move, vert_move) in moves:
                row_new = start_row + side_move
                col_new = start_col + vert_move
                
                # knight stays on board - valid
                if in_bounds(row_new, col_new):
                    prob_still_on += dp(row_new, col_new, moves_remaining-1) * 0.125

            # store prob
            memo[(start_row, start_col, moves_remaining)] = prob_still_on

            return prob_still_on
    

        return dp(row, column, k)
