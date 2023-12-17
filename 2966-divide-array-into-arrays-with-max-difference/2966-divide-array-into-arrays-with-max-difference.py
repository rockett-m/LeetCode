class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:

        if len(nums) % 3 != 0: return []
        
        ans = []
        nums.sort()
        
        for idx in range(0, len(nums), 3):
            if abs(nums[idx] - nums[idx+2]) <= k:
                ans.append([nums[idx], nums[idx+1], nums[idx+2]])
            else:
                return []
        return ans