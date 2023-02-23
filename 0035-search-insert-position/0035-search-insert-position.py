class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        if target in nums:
            return nums.index(target)
        
        li = [-1, -1]
        for i, j in enumerate(nums):
            # print(i, j)
            if target > j:
                li = [i, j]
        print(li)

        return li[0] + 1
