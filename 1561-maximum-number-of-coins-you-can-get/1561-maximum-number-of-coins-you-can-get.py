class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles)[int(len(piles)/3):]
        return sum([x for idx, x in enumerate(piles) if idx%2 == 0])
        # count = 0
        # for i in range(0, len(piles), 2):
        #     count += piles[i]
        # return count