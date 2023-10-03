class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        out = []
        for idx, num in enumerate(sorted(nums)):
            if idx % 2 == 0:
                out.append(num)
        return sum(out)