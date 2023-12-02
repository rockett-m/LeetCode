import sys

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        orig = board.copy()
        coordinates = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        new = []
        for ridx, row in enumerate(board):
            rw = []
            for cidx, col in enumerate(row):
                live_neigh = 0

                # valid = []
                for coords in coordinates:
                    r = ridx + coords[0]
                    c = cidx + coords[1]

                    if r > -1 and c > -1 and r < len(board) and c < len(row):
                        live_neigh += orig[r][c]

                if orig[ridx][cidx] == 1 and (live_neigh < 2 or live_neigh > 3): # change
                    rw.append(0)
                elif orig[ridx][cidx] == 0 and live_neigh == 3: # was dead
                    rw.append(1)
                else: # no change
                    rw.append(board[ridx][cidx])
                # print(f'{live_neigh = } ')

            new.append(rw)
        # print(new)
        board.clear()
        board.extend(new)
