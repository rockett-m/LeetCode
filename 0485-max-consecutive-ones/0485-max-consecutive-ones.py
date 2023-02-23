class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count = 0; high_count = 0
        
        for i in range(len(nums)):
            
            if nums[i] != 1:
                count = 0
            else:
                count += 1
        
                if count > high_count:
                    high_count = count                

        return high_count