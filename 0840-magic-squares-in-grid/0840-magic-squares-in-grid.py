class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        # impossible
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0            
        
        def is_distinct(nums: set) -> bool:
            if len(nums) != 9 or min(nums) < 1 or max(nums) > 9:
                return False
            return True
            
        def is_magic(r: int, c: int) -> bool:
            sums, nums = set(), set()
            for idx in range(3):
                left, center, right = \
                    grid[r+idx][c], grid[r+idx][c+1], grid[r+idx][c+2]
                row_sum = left + center + right
                nums.add(left); nums.add(center); nums.add(right)

                col_sum = grid[r][c+idx] + grid[r+1][c+idx] + grid[r+2][c+idx] 
                
                sums.add(row_sum); sums.add(col_sum)

            mid = grid[r+1][c+1]
            diag_top = grid[r][c]   + mid + grid[r+2][c+2]
            diag_bot = grid[r+2][c] + mid + grid[r][c+2]
            sums.add(diag_top); sums.add(diag_bot)

            if len(sums) == 1 and is_distinct(nums):
                return True
            return False

        count = 0
        # valid bounds by construction
        for row in range(0, len(grid)-2):
            for col in range(0, len(grid[row])-2):
                if is_magic(row, col):
                    count += 1

        return count