from collections import OrderedDict

class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        self.memo_no_first = OrderedDict((idx, max(0, val)) for idx, val in enumerate(nums[1:]))
        self.memo_no_last =  OrderedDict((idx, max(0, val)) for idx, val in enumerate(nums[:-1]))
        
        return max(self._memo_rob(nums[1:], len(nums)-2, True), self._memo_rob(nums[:-1], len(nums)-2, False))
        

    def _memo_rob(self, houses, idx: int, no_first: True):

        if no_first:
            for h, (key, val) in enumerate(self.memo_no_first.items()):
                if h == 1:
                    self.memo_no_first[1] = max(self.memo_no_first[0], self.memo_no_first[1])
                elif h > 1:
                    self.memo_no_first[h] = max(self.memo_no_first[h-1], self.memo_no_first[h] + self.memo_no_first[h-2])
            
        else:
            for h, (key, val) in enumerate(self.memo_no_last.items()):
                if h == 1:
                    self.memo_no_last[1] = max(self.memo_no_last[0], self.memo_no_last[1])
                elif h > 1:
                    self.memo_no_last[h] = max(self.memo_no_last[h-1], self.memo_no_last[h] + self.memo_no_last[h-2])

        return self.memo_no_first[idx] if no_first else self.memo_no_last[idx]
