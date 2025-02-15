class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # mark everyone True if they've held the ball
        friends = [False]*n
        friends[0] = True

        i = 1
        idx_curr = 0
        while True:
            idx_curr = (idx_curr + i*k) % n
            # receives the ball for the 2nd time (game over)
            if friends[idx_curr]: break
            # mark as seen
            friends[idx_curr] = True
            i += 1
    
        # convert to 1-indexing and return those which haven't held ball (False)
        return [(i+1) for i in range(n) if not friends[i]]
