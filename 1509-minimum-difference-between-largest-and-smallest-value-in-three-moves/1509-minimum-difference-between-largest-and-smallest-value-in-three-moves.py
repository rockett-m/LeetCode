class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4 or len(set(nums)) == 1:
            return 0

        nums.sort()

        def dp(lp: int, rp: int, moves_left: int) -> int:
            min_diff = nums[rp] - nums[lp]
            # terminate condition
            if moves_left <= 0 or min_diff == 0:
                return min_diff
            
            return min(dp(lp+1, rp,   moves_left-1),
                       dp(lp,   rp-1, moves_left-1))

        return dp(lp=0, rp=len(nums)-1, moves_left=3)
