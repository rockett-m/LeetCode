# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

global row, col, rmin, cmin, rmax, cmax, r, d, l, u


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        out = [[-1]*n for _ in range(m)]

        global row, col, rmin, cmin, rmax, cmax, r, d, l, u

        row, col = 0, 0
        rmin, cmin, rmax, cmax = 0, 0, m-1, n-1
        r, d, l, u = True, False, False, False

        while head:
            if row == 0 and col == 0:
                out[row][col] = head.val
                head = head.next
                if not head:
                    break

            self.findNext()
            out[row][col] = head.val
            
            head = head.next

        return out
    
    def findNext(self):
        global row, col, rmin, cmin, rmax, cmax, r, d, l, u

        if row == rmin and r: # top row, go right
            if col < cmax: col += 1 # go right
            else: # go down
                row += 1
                rmin += 1
                r = False; d = True

        elif col == cmax and d: # right col, go down
            if row < rmax: row += 1 # go down
            else: # go left
                col -= 1
                cmax -= 1
                d = False; l = True

        elif row == rmax and l: # bottom row, go left
            if col > cmin: col -= 1 # go left
            else: # go up
                row -= 1
                rmax -= 1
                l = False; u = True

        elif col == cmin and u: # left col, go up
            if row > rmin: row -= 1 # col edge, go up
            else:
                col += 1
                cmin += 1 # go right, adjust furthest col
                u = False; r = True

