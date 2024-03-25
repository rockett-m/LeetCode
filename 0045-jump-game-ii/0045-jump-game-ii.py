class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps, loc, far = 0, 0, 0
        if len(nums) == 1: return jumps
        for idx, val in enumerate(nums):
            far = max(far, idx+val)

            if idx == loc:
                loc = far
                jumps += 1

                if loc >= len(nums) - 1:
                    return jumps
