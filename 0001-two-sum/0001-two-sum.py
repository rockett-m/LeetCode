from collections import OrderedDict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # """ slow
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)): # don't compare anything we've seen before with num[i]
                if nums[i] + nums[j] == target:
                    return [i, j]
        # """
        
        """ slower
        dict = OrderedDict()

        for i in range(len(nums)):
            dict[i] = target - nums[i]       # index as key

            for k, v in dict.items():
                if (k != i) and (v == nums[i]):
                    return [i, k]        
        """