class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        count = 0

        for i in range(len(nums)):
            if i.bit_count() == k:
                count += nums[i]

        return count