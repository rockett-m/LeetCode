class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        # return key of min value == 1
        return c.most_common()[:-len(nums)-1:-1][0][0]