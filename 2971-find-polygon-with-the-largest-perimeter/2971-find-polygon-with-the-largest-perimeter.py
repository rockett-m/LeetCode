class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        
        right = len(nums)-1
        while right >= 2:
            
            if nums[right] < sum(nums[0:right]):
                return sum(nums[0:right+1])
            else:
                right -= 1

        return -1