class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0

        for i in range(0, len(nums)-2):
            for j in range(1, len(nums)-1):
                for k in range(2, len(nums)):
                    if not(i < j < k):
                        continue

                    if nums[j] - nums[i] == diff == nums[k] - nums[j]:
                        count += 1

        return count
