class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rx = {}
        cx = {}
        
        # distinct nums per row
        for r in range(len(board)):
            rk = str(r)
            if rk not in rx.keys():
                rx[rk] = [ x for x in board[r] if x != '.' ]
                      
            # distinct nums per col
            for c in range(len(board[r])):
                ck = str(c)
                if r == 0:
                    cx[ck] = []
                if board[r][c] != '.':
                    cx[ck].append(board[r][c])

        # uniq row, col validation
        for rv, cv in zip(rx.values(), cx.values()):
            if len(rv) != len(set(rv)): return False
            if len(cv) != len(set(cv)): return False

        # 3x3 grids
        g1, g2, g3 = [], [], []
        for h in range(len(board)):

            g1 += [ x for x in board[h][0:3] if x != '.' ]
            g2 += [ x for x in board[h][3:6] if x != '.' ]
            g3 += [ x for x in board[h][6:9] if x != '.' ]
            
            if (h+1) % 3 == 0:
                for g in [g1, g2, g3]:
                    print(g)
                    if len(g) != len(set(g)): return False
                g1, g2, g3 = [], [], []

        return True