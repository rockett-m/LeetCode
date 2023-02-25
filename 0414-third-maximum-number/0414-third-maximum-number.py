from collections import Counter
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        if len(nums) < 3:
            return max(nums)

        high_to_low = sorted(list(set(nums)), reverse=True)
        if len(high_to_low) >= 3:
            return high_to_low[2]
        else:
            return high_to_low[0]
