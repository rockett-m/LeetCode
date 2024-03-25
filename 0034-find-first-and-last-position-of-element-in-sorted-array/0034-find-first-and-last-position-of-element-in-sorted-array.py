class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]
        found = False
        for idx, val in enumerate(nums):
            if not found and val == target:
                ans = [idx, idx]
                found = True
            elif found and val == target:
                ans[1] = idx

        return ans