class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        if len(nums) == 1:
            return nums[0] * nums[0]
        elif len(nums) == 2:
            if m == 2:
                return nums[0] * nums[-1]
            return max(nums[0] ** 2, nums[-1] ** 2)
        elif m == 1:                
            return max(max(nums) ** 2, min(nums) ** 2)

        max_first = -100_000
        min_first = 100_000
        high = -min_first**2

        for idx, last in enumerate(nums[m-1:]):

            first = nums[idx]

            max_first = max(max_first, first)
            min_first = min(min_first, first)

            high = max(high, max(min_first * last, max_first * last))
        
        return high
