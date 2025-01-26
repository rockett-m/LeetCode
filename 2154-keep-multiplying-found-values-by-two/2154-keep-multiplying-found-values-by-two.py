class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        curr = original
        maxx = max(nums)
        while curr <= maxx:
            if curr in nums:
                curr *= 2
            else:
                break

        return curr
