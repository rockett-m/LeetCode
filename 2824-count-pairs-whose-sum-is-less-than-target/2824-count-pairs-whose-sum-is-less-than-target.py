class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        for idx, val in enumerate(nums):
            for x, v in enumerate(nums):
                if x > idx and x < len(nums) and val + v < target:
                    count += 1
        return count