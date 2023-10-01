class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = [ x for x in range(0, len(nums)+1)]
        # print(expected, nums)
        for num in range(len(expected)):
            if expected[num] not in nums:
                return expected[num]
