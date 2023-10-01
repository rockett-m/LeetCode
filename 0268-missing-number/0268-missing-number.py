class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # expected = 
        return list(set([ x for x in range(0, len(nums)+1)]) ^ set(nums))[0]

