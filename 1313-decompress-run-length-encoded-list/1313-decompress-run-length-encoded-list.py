class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        arr = []; freq = 0; value = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                freq = nums[i]
            else:
                value = nums[i]
                for i in range(freq):
                    arr.append(value)
                # freq = 0; value = 0
        return arr