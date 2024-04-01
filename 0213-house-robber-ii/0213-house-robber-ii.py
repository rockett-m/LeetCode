from collections import OrderedDict

class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        self.memo_no_first = OrderedDict((idx, max(0, val)) for idx, val in enumerate(nums[1:]))
        self.memo_no_last =  OrderedDict((idx, max(0, val)) for idx, val in enumerate(nums[:-1]))
        
        i = len(nums[1:])-1

        return max(self._memo_rob(nums[1:], i, True), self._memo_rob(nums[:-1], i, False))
        

    def _memo_rob(self, houses, idx: int, no_first: True):

        if no_first:
            for h in range(1, idx+1):
                if h == 1:
                    self.memo_no_first[1] = max(self.memo_no_first[0], self.memo_no_first[1])
                else:
                    self.memo_no_first[h] = max(self.memo_no_first[h-1], self.memo_no_first[h] + self.memo_no_first[h-2])
            
        else:
            for h in range(1, idx+1):
                if h == 1:
                    self.memo_no_last[1] = max(self.memo_no_last[0], self.memo_no_last[1])
                else:
                    self.memo_no_last[h] = max(self.memo_no_last[h-1], self.memo_no_last[h] + self.memo_no_last[h-2])

        return self.memo_no_first[idx] if no_first else self.memo_no_last[idx]
