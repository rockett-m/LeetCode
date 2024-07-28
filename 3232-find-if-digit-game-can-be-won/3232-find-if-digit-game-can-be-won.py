class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = 0
        double = 0
        for idx, val in enumerate(nums):
            if val < 10:
                single += val
            else:
                double += val
        return True if single != double else False