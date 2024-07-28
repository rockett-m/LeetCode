class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single, double = 0, 0
        for _, val in enumerate(nums):
            if val < 10:
                single += val
            else:
                double += val
        return True if single != double else False