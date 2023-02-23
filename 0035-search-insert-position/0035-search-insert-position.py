class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        if target in nums:
            return nums.index(target)
        
        li = [-1, -1]
        for i, j in enumerate(nums):
            if target > j:
                li = [i, j]

        return li[0] + 1
