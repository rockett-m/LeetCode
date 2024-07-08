class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1: return n
        
        circle = [ x for x in range(1, n+1) ]
        
        # using 0-indexing
        start = 0
        while len(circle) > 1:
            # inclusive of curr idx so k-1 hops
            start = (start + k-1) % (len(circle))
            circle.pop(start)

        return circle[0]