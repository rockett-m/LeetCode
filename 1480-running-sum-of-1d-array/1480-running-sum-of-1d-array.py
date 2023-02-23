class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        self.nums = nums
        for i in range(len(nums)):
            if i == 0:
                self.nums[i] = nums[i]
            else:
                self.nums[i] = nums[i-1] + nums[i]
        
        return self.nums