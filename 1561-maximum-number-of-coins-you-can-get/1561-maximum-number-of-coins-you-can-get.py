class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        return sum([x for idx, x in enumerate(sorted(piles)[int(len(piles)/3):]) if idx % 2 == 0])