class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(0, (max(nums)-2*k) - (min(nums)))