class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        idx = nums.index(max(nums))
        maxx = nums.pop(idx)
        return idx if maxx >= 2*max(nums) else -1

