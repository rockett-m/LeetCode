class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = [ x for x in range(0, len(nums)+1)]
        return list(set(expected) ^ set(nums))[0]

