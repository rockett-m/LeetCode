class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        # commented out is not any faster than this
        # return sum([sum(nums[max(0, i-nums[i]):i+1]) for i in range(len(nums))])
        ans = 0
        starts = [max(0, i-nums[i]) for i in range(len(nums))]
        for i in range(len(nums)):
            ans += sum(nums[starts[i]:i+1])
        return ans