class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        # for idx, val in enumerate(sorted(nums)):
        #     nums[idx] = nums[idx] + k, -k
            
        return max(0, (max(nums)-k) - (min(nums)+k))