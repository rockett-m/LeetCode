class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        evens = 0
        
        # for x in range(6):
        #     for i in range(len(nums)):
        #        if ((x % 2 != 0) and ((nums[i] >= 10**(x)) and (nums[i] < 10**(x+1)))):
        #             evens += 1
        
        for item in nums:
            if len(str(item)) % 2 == 0:
                evens += 1
        return evens