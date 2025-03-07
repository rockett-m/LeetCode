class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid

    def adjacentSum(self, value: int) -> int:
        total = 0
        row, col = self.findValIdx(value)
        for coords in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
            r, c = coords[0], coords[1]
            if 0 <= row + r < len(self.grid) and \
                0 <= col + c < len(self.grid):
                total += self.grid[row+r][col+c]

        return total

    def diagonalSum(self, value: int) -> int:
        total = 0
        row, col = self.findValIdx(value)
        for coords in [[-1, -1], [-1, 1], [1, -1], [1, 1]]:
            r, c = coords[0], coords[1]
            if 0 <= row + r < len(self.grid) and \
                0 <= col + c < len(self.grid):
                total += self.grid[row+r][col+c]

        return total

    def findValIdx(self, value: int) -> Tuple[int, int]:
        for r in range(len(self.grid)):
            for c in range(len(self.grid)):
                if self.grid[r][c] == value:
                    return r, c

        return None, None            

# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)