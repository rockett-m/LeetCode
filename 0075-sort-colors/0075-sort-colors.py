class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros, ones = False, False
        c = Counter(nums)
        for idx, val in enumerate(nums):
            if c[0] > 0:
                nums[idx] = 0
                c[0] -= 1
            elif c[1] > 0:
                nums[idx] = 1
                c[1] -= 1
            else:
                nums[idx] = 2
            