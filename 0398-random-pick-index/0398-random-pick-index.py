class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.mydict = {}
        for idx, val in enumerate(self.nums):
            if val not in self.mydict:
                self.mydict[val] = []
            self.mydict[val].append(idx)

    def pick(self, target: int) -> int:
        return random.choice(self.mydict[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)