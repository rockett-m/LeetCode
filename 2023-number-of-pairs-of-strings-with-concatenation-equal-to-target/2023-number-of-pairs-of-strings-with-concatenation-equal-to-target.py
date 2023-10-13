class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = 0
        left, right = 0, 0
        for idx, val in enumerate(nums):
            for i, v in enumerate(nums):
                if idx != i: # can't compare same index
                    ans = nums[idx] + nums[i]
                    if ans == target: count += 1

        return count