class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        i = 0
        count = False
        dist = 0

        while i < len(nums):
            if nums[i] == 0:
                if count:
                    dist += 1

            else: # nums[i] == 1
                # immediate fail if count and dist < k
                if count and dist < k:
                    return False
                else:
                    count = True
                    dist = 0

            i += 1

        return True
