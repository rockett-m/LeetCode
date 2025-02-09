class Solution:
    def __init__(self):
        self.height = 0
        self.width = 0

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.height = len(grid) 
        self.width = len(grid[0]) 
        peri = 0

        for r in range(self.height):
            for c in range(self.width):
                # can't analyze water
                if grid[r][c] == 0: continue

                peri += self.count_block(grid, r, c)

        return peri

    def count_block(self, grid, r, c) -> int:
        """ returns between 0 and 4 """
        add_perim = 0
        # water (accounted for in main fn too) or invalid
        if grid[r][c] == 0: return 0
        if not (0 <= r <= self.height-1): return 0
        if not (0 <= c <= self.width-1): return 0

        # any land on border edge will have +1 perim on each side
        # +1 to land if water is adjacent to an edge 
        # 1-1 for land-land = 0 (nothing added) but 
        # 1-0 for land-water = 1 (adds 1 to perim)
        oob_count = 0
        if r-1 < 0:
            oob_count += 1
        else:
            add_perim += (1 - grid[r-1][c])
        if r+1 > self.height-1:
            oob_count += 1
        else:
            add_perim += (1 - grid[r+1][c])
        if c-1 < 0:
            oob_count += 1
        else:
            add_perim += (1 - grid[r][c-1])
        if c+1 > self.width-1:
            oob_count += 1
        else:
            add_perim += (1 - grid[r][c+1])     

        add_perim += oob_count
        # print(f'grid[{r=}][{c=}] = {grid[r][c]}')
        return add_perim
